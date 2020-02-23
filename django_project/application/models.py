from django.db import models

# Create your models here.

class Signup(models.Model):
    user_email = models.CharField(max_length=25)
    user_name = models.CharField(max_length=25)
    user_age = models.IntegerField()
    user_city = models.CharField(max_length=25)
