from django.db import models

# Create your models here.


class User (models.Model):
    name = models.CharField()
    email = models.CharField()
    password = models.CharField()
    salt = models.CharField()
    bio = models.CharField()


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
