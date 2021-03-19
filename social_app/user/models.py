from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=64)
    email = models.EmailField()
    password = models.CharField(max_length=999)
    gender = models.CharField(max_length=1)
    profile_image = models.CharField(max_length=256, default="noimg.jpg", editable=False)
    followers = models.IntegerField(default=0, blank=False)
    followings = models.IntegerField(default=0, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Name {self.name} , Email: {self.email}"
