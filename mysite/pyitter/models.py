from django.db import models

# Create your models here.


class User (models.Model):
    name = models.CharField(max_length=30)
    email = models.TextField()
    password = models.TextField()
    salt = models.TextField()
    bio = models.TextField()


class Tweet (models.Model):
    user_id = models.ForeignKey(User)
    content = models.CharField(max_length=200)


"""
class Follow(models.Model):
    user_id = models.ForeignKey(User)
    following_id = models.Integer()


class Favorite(models.Model):
    tweet = models.ForeignKey(Tweet)
    user = models.ForeignKey(User)
"""
