from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .serializers import BookSerializer, MemberSerializer
from .models import Book, Member
from rest_framework.filters import OrderingFilter, SearchFilter


class Books(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    filterset_fields = ['title']
    search_fields = ['author']
    

class BookDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
    lookup_field = 'pk'
    

class Members(ListCreateAPIView):
    queryset = Member.objects.all()
    serializer_class = MemberSerializer
    filter_backends = [OrderingFilter, SearchFilter]
    filterset_fields = ['full_name', 'phone']
    search_fields = ['full_name']
    
    
class MemberDetails(RetrieveUpdateDestroyAPIView):
    serializer_class = MemberSerializer
    queryset = Member.objects.all()
    lookup_field = 'pk'
    