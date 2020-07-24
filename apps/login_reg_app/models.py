from django.db import models

# Create your models here.
from django.db import models
import re
import bcrypt
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
class UserManager(models.Manager):
    def validate_user(self, postData):
        errors = {}
        check = User.objects.filter(email=postData['email'])
        if len(postData['first_name']) < 2 or not postData['first_name'].isalpha():
            errors['first_name'] = "First name must be at least 2 characters and letters only"
        if len(postData['last_name']) < 2 or not postData['last_name'].isalpha():
            errors['last_name'] = "Last name must be at least 2 characters and letters only"
        if len(postData['password']) < 8:
            errors['password'] = "Your password must be at least 8 characters."
        elif postData['password'] != postData['conf_password']:
            errors['conf_password'] = "Your password and confirm password must match."
        if len(postData['email']) < 1:
            errors['email'] = "Email field can't be blank."
        elif not EMAIL_REGEX.match(postData['email']):         
            errors['email'] = "Invalid email address!"
        elif check:
            errors['email'] = 'Email address is already registered'
        return errors
    
    def validate_login(self, postData):
        errors = {}
        check_user = User.objects.filter(email=postData['email'])
        if not check_user:
            errors['login_email'] = "Email has not been registered"
        else:
            if not bcrypt.checkpw(postData['password'].encode(), check_user[0].password.encode()): 
                errors['login_email'] = "Email and password do not match"
        return errors
class User(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()