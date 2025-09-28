from rest_framework import serializers
from .models import Book, Student, User, Borrowing


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = "__all__"
        
        
class StudentSerializer(serializers.ModelField):
    class Meta:
        model = Student
        fields = "__all__"
        
class UserSerializer(serializers.ModelField):
    class Meta:
        model = User
        fields = "__all__"
    
    
class BorrowingSerializer(serializers.ModelField):
    class Meta:
        model = Borrowing
        fields = "__all__"
    