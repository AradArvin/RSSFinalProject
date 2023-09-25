from rest_framework import serializers
from django.contrib.auth import authenticate
from rest_framework import status
from .models import CustomUser
from .utils import *




class RegisterationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    confirm_password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'confirm_password']

    def create(self, validated_data):
        """Create a user from the validated data that anonuser entered."""

        return CustomUser.objects.create_user(**validated_data)

    
    class Meta:
        pass



class SignUpUserSerializer(serializers.ModelSerializer):
    class Meta:
        pass