from rest_framework import serializers
from .models import Book
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
    