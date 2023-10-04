from rest_framework import serializers
from .models import *



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"




class BookMarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = BookMark
        exclude = ("user",)



class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = "__all__"