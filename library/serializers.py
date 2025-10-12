from rest_framework import serializers
from .models import Book, Member, Lend
from datetime import date

class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        
    def validate_isbn(self, value):
        book_id = self.instance.id if self.instance else None
        if Book.objects.exclude(id=book_id).filter(isbn=value).exists():
            raise serializers.ValidationError("ISBN already exists.")
        return value
    
    def validate_published_date(self, value):
        if value > date.today():
            raise serializers.ValidationError("Published date cannot be in the future")
        return value
    
    
class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member
        fields = "__all__"
        
        

class LendSerializer(serializers.ModelSerializer):
    book = BookSerializer(read_only=True)
    member = MemberSerializer(read_only=True)
    is_overdue = serializers.ReadOnlyField()
    
    book_id = serializers.PrimaryKeyRelatedField(
        queryset=Book.objects.all(), source='book', write_only=True
    )
    member_id = serializers.PrimaryKeyRelatedField(
        queryset=Member.objects.all(), source='member', write_only=True
    )

    class Meta:
        model = Lend
        fields = [
            'id', 'lent_date', 'return_date', 'book', 'member', 
            'book_id', 'member_id', 'status', 'is_overdue'
        ]

    def validate_return_date(self, value):
        if value < date.today():
            raise serializers.ValidationError('Return date cannot be in the past')
        return value

    def validate(self, attrs):
        """Check if the book has available copies before lending."""
        book = attrs.get('book')
        if book.available_copies is None or book.available_copies <= 0:
            raise serializers.ValidationError(
                f"Book '{book.title}' has no available copies."
            )
        return attrs

    def create(self, validated_data):
        """Reduce available copies when a book is lent."""
        book = validated_data['book']
        
        # Reduce available copies
        book.available_copies -= 1
        if book.available_copies <= 0:
            book.status = False
        book.save()

        # Create the lending record
        lend = Lend.objects.create(**validated_data)
        return lend
    
    
class ReturnBookSerializer(serializers.ModelSerializer):
    book_title = serializers.CharField(source='book.title', read_only=True)
    member_name = serializers.CharField(source='member.full_name', read_only=True)

    class Meta:
        model = Lend
        fields = ['id', 'book_title', 'member_name', 'returned_at']
        
    