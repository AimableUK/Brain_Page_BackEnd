from django.urls import path
from library.views import (
    Books, 
    BookDetails, 
    Students, 
    StudentDetails, 
    Users, 
    UserDetails,
    Borrowings,
    BorrowingDetails,
    ReturnBook
)

urlpatterns = [
    # Book
    path('books/', Books.as_view(), name="book-list" ),
    path('books/<int:pk>/', BookDetails.as_view(), name="book-details" ),
    
    # Student
    path('students/', Students.as_view(), name="student-list" ),
    path('students/<int:pk>/', StudentDetails.as_view(), name="student-details" ),
    
    # User
    path('users/', Users.as_view(), name="user-list" ),
    path('users/<int:pk>/', UserDetails.as_view(), name="user-details" ),
    
    # Borrowing
    path('borrow/', Borrowings.as_view(), name="borrow-list-create"),
    path('borrow/<uuid:pk>/', BorrowingDetails.as_view(), name="borrow-detail"),
    path('borrow/<uuid:pk>/return/', ReturnBook.as_view(), name="return-book"),
]
