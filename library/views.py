from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer, StudentSerializer, UserSerializer, BorrowingSerializer
from .models import Book, Student, User, Borrowing
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.utils import timezone
from rest_framework.permissions import AllowAny

# ---- Books ---- #
class Books(generics.ListCreateAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    
class BookDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'pk'


# ---- Students ---- #
class Students(generics.ListCreateAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    
class StudentDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()
    lookup_field = 'pk'


# ---- Users ---- #
class Users(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    
class UserDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    lookup_field = 'pk'
    
    
# ---- Borrowings ---- #
class Borrowings(generics.ListCreateAPIView):
    serializer_class = BorrowingSerializer
    queryset = Borrowing.objects.all()
    
class BorrowingDetails(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = BorrowingSerializer
    queryset = Borrowing.objects.all()
    lookup_field = 'pk'
    
class ReturnBook(generics.UpdateAPIView):
    queryset = Borrowing.objects.all()
    serializer_class = BorrowingSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        borrowing = self.get_object()
        if borrowing.status == "returned":
            raise serializers.ValidationError("Book already returned")
        borrowing.status = "returned"
        borrowing.return_date = timezone.now()
        borrowing.book.available_copies += 1
        borrowing.book.save()
        borrowing.save()
        