from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Employee(models.Model):
    code=models.CharField(max_length=20)
    first_name=models.CharField(max_length=80)
    middle_name=models.CharField(max_length=80)
    last_name=models.CharField(max_length=80)

    def __str__(self):
        return self.last_name