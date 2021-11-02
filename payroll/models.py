from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model
from django.db.models.fields import CharField
# Create your models here.

class Employee(models.Model):
    code=models.CharField(max_length=20)
    first_name=models.CharField(max_length=80)
    middle_name=models.CharField(max_length=80)
    last_name=models.CharField(max_length=80)
    company=models.CharField(max_length=120)
    company_branch=models.CharField(max_length=12)
    ssnit_number=models.CharField(max_length=13)
    national_id=models.CharField(max_length=40)
    gra_tin=models.CharField(max_length=40)
    
    def __str__(self):
        return self.last_name

class Affordability(models.Model):
    employee_number=models.CharField(max_length=20)
    staff_id=models.CharField(max_length=20)
    name=models.CharField(max_length=120)
    ssf_number=models.CharField(max_length=13)
    monthly_afford=models.DecimalField(decimal_places=2,max_digits=8)
    running_afford=models.DecimalField(decimal_places=2,max_digits=8)
    period=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name +': '+ self.period+'-'+self.monthly_afford+'-'+self.running_afford

class UserGroups(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    group_id=models.IntegerField()

class ActivityLog(models.Model):
    username=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    description=models.CharField(max_length=200)
    created=models.DateTimeField(auto_created=True)

class LoginAttempts(models.Model):
    ip_address=models.CharField(max_length=39,default='0')
    timestamp=models.DateTimeField(blank=True)
    attempts=models.SmallIntegerField()


