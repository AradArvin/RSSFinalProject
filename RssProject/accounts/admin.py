from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(CustomUser)
class CustomUserDisplay(admin.ModelAdmin):
    pass


@admin.register(Notif)
class NotifDisplay(admin.ModelAdmin):
    pass


@admin.register(UserNotif)
class UserNotifDisplay(admin.ModelAdmin):
    pass