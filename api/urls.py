from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),
    
    # Book
    # path('books/', Books.as_view(), name="book-list" ),
    # path('books/<int:pk>/', BookDetails.as_view(), name="book-details" ),

    # # User
    # path('users/', Users.as_view(), name="user-list" ),
    # path('users/<int:pk>/', UserDetails.as_view(), name="user-details" ),
    
    # Borrowing
    # path('borrow/', Borrowings.as_view(), name="borrow-list-create"),
    # path('borrow/<uuid:pk>/', BorrowingDetails.as_view(), name="borrow-detail"),
    # path('borrow/<uuid:pk>/return/', ReturnBook.as_view(), name="return-book"),
]
