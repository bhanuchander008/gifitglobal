from django.db import models

# Create your models here.
from django.db import models
from django.db import models

import uuid



class Roles(models.Model):
    name = models.CharField(max_length= 250)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by =models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)
    is_active =  models.BooleanField(default=False)


class Users(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),)

    FirstName  = models.CharField(max_length= 250)
    LastName   = models.CharField(max_length=250)
    Gender     = models.CharField(max_length=1, choices=GENDER_CHOICES)
    dob        =  models.CharField(max_length= 250)
    nationality = models.CharField(max_length= 250)
    email      = models.EmailField(unique=True)
    password   = models.CharField(max_length=250)
    locked = models.CharField(max_length= 250)
    failed_attempts = models.IntegerField()
    point_balance = models.FloatField()
    lastlogin_at = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_by =models.DateTimeField(auto_now_add=True)
    updated_by = models.DateTimeField(auto_now=True)
    is_active =  models.BooleanField(default=False)



class File(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    file = models.FileField(blank=False, null=False)

    def __str__(self):
        return self.file.name
