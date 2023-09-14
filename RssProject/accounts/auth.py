'''
JWT Authentication

1 - customuser model creation

2 - set default user to customuser in settings.py

3 - create a custom authentication backend for jwt

class JWTAuthentication(...):
    
    def authenticate(self, request):
        pass
        
    def authentication_header(self, request):
        pass
        
    @classmethod
    def create_jwt(cls, user):
        pass
        
    @classmethod
    def get_token_from_header(cls, token):
        pass

        
4 - activate authentication class by setting it as a default authentication class of rest framework.


REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'apps.management.authentication.JWTAuthentication',
    ]
}


5 - serializer for login and register users

6 - create token api view

class ObtainTokenView(views.APIView):

    def post(self, request, *args, **kwargs):
        pass
        
7 - test by postman

'''



