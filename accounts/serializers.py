from dj_rest_auth.registration.serializers import RegisterSerializer
from rest_framework import serializers
from accounts.models import Account

class CustomRegisterSerializer(RegisterSerializer):
    email = serializers.EmailField(required=True)
    username = serializers.CharField(required=True)

    def get_cleaned_data(self):
        validated_data = getattr(self, "validated_data", {}) or {}
        
        data = super().get_cleaned_data()
        data['username'] = validated_data.get('username', '')
        data['email'] = validated_data.get('email', '')
        return data
