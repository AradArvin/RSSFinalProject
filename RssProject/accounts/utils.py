import jwt
from datetime import datetime, timedelta
from uuid import uuid4
from django.conf import settings
from django.core.cache import cache
from typing import Any
from rest_framework.exceptions import APIException


class WrongToken(APIException):
    status_code = 401
    default_detail = 'Not Acceptable'
    default_code = '403'


class TokenNotFound(APIException):
    status_code = 404
    default_detail = 'Not Found'
    default_code = '403'


