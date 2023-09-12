from django.contrib.auth.models import BaseUserManager



class CustomUserManager(BaseUserManager):
    def create_user(self, username, email, password, **other_fields):
        other_fields.setdefault('is_active', True)

        if not email:
            raise ValueError('Please provide an Email adress')

        user = self.model(email=email, username=username, **other_fields)
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password, **other_fields):
        
        other_fields.setdefault('is_staff', True)
        other_fields.setdefault('is_superuser', True)
        other_fields.setdefault('is_active', True)

        user = self.create_user(self, username, email, password, **other_fields)
        
        return user