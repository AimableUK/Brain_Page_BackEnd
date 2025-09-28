from django.shortcuts import render
from rest_framework import generics
from .serializers import BookSerializer, StudentSerializer, UserSerializer, BorrowingSerializer
from .models import Book, Student, User, Borrowing


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
    