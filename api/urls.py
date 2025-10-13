from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView, TokenRefreshView, TokenVerifyView
)
from library.views import (
    Books, BookDetails, Members, MemberDetails,
    Lends, LendDetails, ReturnBook
)
from dj_rest_auth.registration.views import SocialLoginView
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter


class GoogleLogin(SocialLoginView):
    adapter_class = GoogleOAuth2Adapter


urlpatterns = [
    # Google auth
    path('google/', GoogleLogin.as_view(), name='google_login'),

    # JWT endpoints
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # dj-rest-auth
    path('auth/', include('dj_rest_auth.urls')),
    path('auth/registration/', include('dj_rest_auth.registration.urls')),

    # Books
    path('books/', Books.as_view(), name="book-list"),
    path('books/<int:pk>/', BookDetails.as_view(), name="book-details"),

    # Members
    path('members/', Members.as_view(), name="member-list"),
    path('members/<int:pk>/', MemberDetails.as_view(), name="member-details"),

    # Lends
    path('lends/', Lends.as_view(), name="lends-list-create"),
    path('lends/<int:pk>/', LendDetails.as_view(), name="lend-details"),
    path('return/<int:pk>/', ReturnBook.as_view(), name="return-book"),
]
