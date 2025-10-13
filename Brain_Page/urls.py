from django.contrib import admin
from django.urls import path, include, re_path
from django.conf.urls.static import static
from django.conf import settings
from allauth.account.views import confirm_email as allauth_confirm_email


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('api.urls')),
    path('accounts/', include('allauth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    
    # Custom email confirm override (avoid template error)
    re_path(
        r'^dj-rest-auth/registration/account-confirm-email/(?P<key>[-:\w]+)/$',
        allauth_confirm_email,
        name='account_confirm_email',
    ),
    
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
