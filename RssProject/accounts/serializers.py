from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth.hashers import check_password
from django.conf import settings
from django.utils.translation import gettext_lazy as _
from uuid import uuid4

from .models import CustomUser
from .utils import *
from .tasks import send_feedback_email_task
from .publishers import publisher


class RegisterationSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    confirm_password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'username', 'password', 'confirm_password']

    def create(self, validated_data):
        """Create a user from the validated data that anonuser entered."""

        return CustomUser.objects.create_user(**validated_data)

    


class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField()
    password = serializers.CharField(max_length=128, write_only=True)
    access = serializers.CharField(max_length=512, read_only=True)
    refresh = serializers.CharField(max_length=512, read_only=True)


    def validate(self, attrs):
        """Validate entered user data and generate refresh and access token for user."""

        email = attrs.get('email', None)
        password = attrs.get('password', None)

        if email is None:
            raise serializers.ValidationError(_("An email adress is required to login"))
       
        if password is None:
            raise serializers.ValidationError(_("A password is required to login"))
        

        user = authenticate(username=email, password=password)
        

        if user is None:
            raise serializers.ValidationError(_("User not found! Please check your email or password."))
        

        if check_cache(user.id):
            raise serializers.ValidationError(_("The user is already logged in!")) 


        if not user.is_active:
            raise serializers.ValidationError(_("This user has been deavtivated"))
        
        access_token = access_token_gen(user.pk)
        refresh_token = refresh_token_gen(user.pk)

        cache_setter(refresh_token)

        log_data = {
                "username": user.username,
                "message": f"User: {user.username} successfull login",
                "status": "login"
            }
        publisher(log_data)

        validated_data = {
            'email': user.email,
            'username': user.username,
            'access': access_token,
            'refresh': refresh_token,
        }
    
        return validated_data
    



class UserRUSerializer(serializers.ModelSerializer):

    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    id = serializers.IntegerField(read_only=True)

    class Meta:
        model = CustomUser
        fields = ['id', 'email', 'username', 'password']
        # read_only_fields = ('token',)


    def update(self, instance, validated_data):
        """Update a user with new data."""

        password = validated_data.pop('password', None)

        for key, value in validated_data.items():
            setattr(instance, key, value)

        if password is not None:
            instance.set_password(password)

        instance.save()

        return instance
    



class RefreshTokenSerializer(serializers.Serializer):
    email = serializers.EmailField(write_only=True)
    password = serializers.CharField(max_length=128, write_only=True)
    refresh_token = serializers.CharField(max_length=512, read_only=True)

    def validate(self, attrs):
        """Provide user data to get refresh token."""

        email = attrs.get('email', None)
        password = attrs.get('password', None)

        if email is None:
            raise serializers.ValidationError(_("An email adress is required to login"))
       
        if password is None:
            raise serializers.ValidationError(_("A password is required to login"))
        
        user = authenticate(username=email, password=password)

        if user is None:
            raise serializers.ValidationError(_("Refresh Token not found! Check if you are logged in."))
        

        if not user.is_active:
            raise serializers.ValidationError(_("This user has been deavtivated"))
        
        refresh_token = cache_getter(user_id=user.id)

        validated_data = {
            'email':user.email,
            'refresh_token': refresh_token,
        }
    
        return validated_data
    



class AccessTokenSerializer(serializers.Serializer):
    refresh_token = serializers.CharField(max_length=512, write_only=True)
    access_token = serializers.CharField(max_length=512, read_only=True)

    def validate(self, attrs):
        """Provide the refresh token  in order to get the access token"""
        refresh_token = attrs.get('refresh_token', None)

        if refresh_token is None:
            raise serializers.ValidationError(_("You must enter the refresh token in order to get access token"))
       
        
        payload = token_decode(refresh_token)
        
        
        user = CustomUser.objects.get(id=payload["user_id"])
        
        if cache_getter(user.id):
        
            access_token = access_token_gen(user_id=user.id)

            validated_data = {
                'email':user.email,
                'access_token': access_token,
            }
        
            return validated_data



class ChangePasswordSerializer(serializers.ModelSerializer):
    password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    new_password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    confirm_new_password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    class Meta:
        model = CustomUser
        fields = ['password', 'new_password','confirm_new_password']



    def update(self, instance, validated_data):
        """Update a user with new data."""

        password = validated_data.pop('password', None)

        if check_password(password, instance.password):
            
            new_password = validated_data.get("new_password", None)
            confirm_new_password = validated_data.get("confirm_new_password", None)

            if new_password and confirm_new_password:
                if new_password == confirm_new_password:
                    instance.set_password(confirm_new_password)
                    instance.save()

                    return instance
                else:
                    raise serializers.ValidationError(_("New Passwords don't match!"))
            else:
                raise serializers.ValidationError(_("New password or confirm password missing!"))
        else:
            raise serializers.ValidationError(_("Old password is wrong!"))
        



class ForgetPasswordSerializer(serializers.Serializer):
    email = serializers.EmailField()

    def validate(self, attrs):
        
        email = attrs.get('email', None)
        user = CustomUser.objects.get(email=email)

        if not user.exists():
            raise serializers.ValidationError(_("User with this email does not exist!"))
        
        msg = f"{settings.BASE_URL}/set-pass/{uuid4().hex}{user.id}/"

        send_feedback_email_task.delay(email, msg)

        return super().validate(attrs)
    



class SetNewPasswordSerializer(serializers.Serializer):
    new_password = serializers.CharField(max_length=128, min_length=8, write_only=True)
    confirm_new_password = serializers.CharField(max_length=128, min_length=8, write_only=True)

    
    def update(self, instance, validated_data):

        new_password = validated_data.get("new_password", None)
        confirm_new_password = validated_data.get("confirm_new_password", None)

        if new_password and confirm_new_password:
            if new_password == confirm_new_password:
                instance.set_password(confirm_new_password)
                instance.save()

                return instance
            else:
                raise serializers.ValidationError(_("Passwords don't match!"))
        else:
            raise serializers.ValidationError(_("password or confirm password missing!"))


        