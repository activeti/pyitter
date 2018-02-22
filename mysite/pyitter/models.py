from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.


class User (AbstractUser):
    salt = models.TextField()
    bio = models.TextField()


class Tweet (models.Model):
    user_id = models.ForeignKey(User)
    content = models.CharField(max_length=200)

    def __str__(self):
        return self.content


"""
class Follow(models.Model):
    user_id = models.ForeignKey(User)
    following_id = models.Integer()


class Favorite(models.Model):
    tweet = models.ForeignKey(Tweet)
    user = models.ForeignKey(User)
"""
