from django.urls import path
from .views import save_to_db

urlpatterns = [
    path("", save_to_db, name="save")
]