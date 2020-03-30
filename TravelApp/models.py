from __future__ import unicode_literals
from django.db import models
from datetime import date, datetime

class UserManager(models.Manager):
    def basic_validator(self, postData):    
        errors = {}
        
        if len(postData['name']) < 3:
            errors['first_name'] = "Name should be at least 3 characters!"

        if len(postData['user_name']) < 3:
            errors['username'] = "Username should be at leat 3 characters!"

        all_users= User.objects.all()
        for x in all_users:
            if x.user_name == postData['user_name']:
                errors['user_name'] = "Username must be unique!"

        if len(postData['password']) < 8:
            errors['password'] = "Password should be at leat 8 characters!"

        if postData['password'] != postData['cpassword']:
            errors['password'] = "Password does not match password password confirm!"

        return errors

class TravelManager(models.Manager):
    def travel_validator(self, postData):
        errors = {}

        if len(postData['destination']) < 1 :
            errors['destination'] = "Destination field can not be empty"

        if len(postData['desc']) < 1 :
            errors['desc'] = "Description field can not be empty"

        if str(date.today()) > str(postData['start']):
            errors['start'] = "Start time can not be in the past"

        if str(date.today()) > postData['end']:
            errors['end'] = "End date must be in the future"

        if postData['start'] > postData['end']:
            errors['start'] = "Travel Date From can not be in the future of Travel Date To"

        return errors

class User(models.Model):
    name = models.CharField(max_length=225)
    user_name = models.CharField(max_length=225)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = UserManager()

class Travel(models.Model):
    destination = models.CharField(max_length=50)
    desc = models.TextField()
    start = models.DateTimeField()
    end = models.DateTimeField()
    creator = models.ForeignKey(User, related_name="plan", on_delete=models.CASCADE)
    join = models.ManyToManyField(User, related_name="join")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now_add=True)
    objects = TravelManager()
