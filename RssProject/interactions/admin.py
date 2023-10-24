from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Comment)
class CommentDisplay(admin.ModelAdmin):
    pass

@admin.register(Like)
class LikeDisplay(admin.ModelAdmin):
    pass


@admin.register(SubScribe)
class SubScribeDisplay(admin.ModelAdmin):
    pass


@admin.register(BookMark)
class BookMarkDisplay(admin.ModelAdmin):
    pass
