from allauth.account.adapter import DefaultAccountAdapter

class MyAccountAdapter(DefaultAccountAdapter):
    def get_phone(self, user):
        # Return None if you don't want phone numbers
        return None
    