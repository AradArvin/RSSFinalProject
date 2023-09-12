from rest_framework import serializers
from .models import CustomUser



class CustomUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = [
            'username', 
            'email',
            'first_name',
            'last_name',
            ]



class LoginUserSerializer(serializers.ModelSerializer):
    class Meta:
        pass



class SignUpUserSerializer(serializers.ModelSerializer):
    class Meta:
        pass