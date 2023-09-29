from django.db import models
from accounts.models import CustomUser
from podcasts.models import *

# Create your models here.



class Comment(models.Model):
    opinion = models.TextField()
    commenter = models.ForeignKey(CustomUser, on_delete=models.CASCADE)



    def __str__(self) -> str:
        return self.opinion[:15]




class Like(models.Model):
    users = models.ManyToManyField(CustomUser)



    def __str__(self) -> str:
        return self.likes.count()



class SubScribe(models.Model):
    subscribed = models.ForeignKey(CustomUser, on_delete=models.CASCADE)





class BookMark(models.Model):
    bookmarked = models.ForeignKey(CustomUser, on_delete=models.CASCADE)

