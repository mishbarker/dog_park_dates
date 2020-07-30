from django.db import models
from apps.login_reg_app.models import User
from datetime import datetime
from datetime import date
import re


class PlaydateManager(models.Manager):
    def validate_playdate(self, postData):
        errors = {}
        if len(postData['park_name']) < 3:
            errors['park_name'] = "Park name must be at least 3 characters."
        if len(postData['comments']) < 3:
            errors['comments'] = "Comments must be at least 3 characters."      
        if postData['date'] =='':
            errors['date'] = "Date field can't be blank."
        if postData['time'] =='':
            errors['time'] = "Time field can't be blank."
        date = datetime.strptime(postData['date'], '%Y-%m-%d').date()
        if date <= date.today():
            errors['date'] = "Date must be in the future"
        return errors

class Playdate(models.Model):
    park_name = models.CharField(max_length=255)
    park_address = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
    comments = models.TextField()
    creator = models.ForeignKey(User, related_name='created_playdate', on_delete=models.CASCADE)
    users_who_joined = models.ManyToManyField(User, related_name="joined_playdates")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = PlaydateManager()

class Dog(models.Model):
    owner = models.ForeignKey(User, related_name='has_dog', on_delete=models.CASCADE)
    name = models.CharField(max_length=100, default="not provided", blank=True, null=True)
    breed = models.CharField(max_length=100, default="not provided", blank=True, null=True)
    gender = models.CharField(max_length=6, default="not provided", blank=True, null=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

