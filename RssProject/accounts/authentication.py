import jwt
from django.conf import settings
from rest_framework import authentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.exceptions import APIException
from .models import CustomUser
from .utils import *


class TokenException(APIException):
    status_code = 401
    default_detail = 'Unauthorized'
    default_code = '403'
