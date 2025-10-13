from allauth.account.adapter import DefaultAccountAdapter
from django.conf import settings

class CustomAccountAdapter(DefaultAccountAdapter):
    def get_phone(self, user):
        # Return None if you don't want phone numbers
        return None
    
    def get_email_confirmation_url(self, request, emailconfirmation):
        key = emailconfirmation.key
        return f"{settings.FRONTEND_URL}/confirm-email?key={key}"
    
    