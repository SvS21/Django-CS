from django.contrib.postgres.fields import JSONField
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from django.core.exceptions import ValidationError
from django.forms import DecimalField
from django.utils import timezone
import datetime

class Teacher(models.Model):
    name = models.CharField(max_length=100, null=False)
    lastName = models.CharField(max_length=100, null=False)
    telephoneNumber = models.IntegerField(null=True)
    age = models.IntegerField(null=False)
    gender = models.CharField(max_length=100, null=False)
    birthday = models.DateField(null=False, default=timezone.now)
    yearsOfExperience = models.IntegerField(null=False)
    delete = models.BooleanField(default = False)
    created = models.DateTimeField(default = timezone.now)
    edited = models.DateTimeField(blank=True, null=True, default=None)

    def __str__(self):
        return self.name

    class Meta: 
        db_table = 'Teacher'
