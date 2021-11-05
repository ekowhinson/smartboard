from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model, ModelStateFieldsCacheDescriptor
from django.db.models.deletion import DO_NOTHING
from django.db.models.fields import BooleanField, CharField
# Create your models here.


class Company(models.Model):
    code=models.CharField(max_length=20)
    name=models.CharField(max_length=200)
    email=models.EmailField()
    contact_number=models.CharField(max_length=30)
    status=models.BooleanField()
    date_created=models.DateTimeField(auto_now=True)
    contact_number1=models.CharField(max_length=30)
    contact_number2=models.CharField(max_length=30)
    ceo_number=models.CharField(max_length=30)
    ceo_name=models.CharField(max_length=120)
    contact_person=models.CharField(max_length=120)
    address=models.CharField(max_length=150)
    postal_address=models.CharField(max_length=150)
    landmark=models.CharField(max_length=200)
    authorization_status=BooleanField()
    authorized_by=models.ForeignKey(User,on_delete=DO_NOTHING)

    def __str__(self):
        return self.code + ': ' +self.name

class CompanyBranch(models.Model):
    company=models.ForeignKey(Company,on_delete=DO_NOTHING)
    branch_name=models.CharField(max_length=120)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return str(self.company) +', '+ self.branch_name



class Employee(models.Model):
    code=models.CharField(max_length=20)
    first_name=models.CharField(max_length=80)
    middle_name=models.CharField(max_length=80)
    last_name=models.CharField(max_length=80)
    company=models.ForeignKey(Company,on_delete=DO_NOTHING)
    company_branch=models.ForeignKey(CompanyBranch,on_delete=DO_NOTHING)
    ssnit_number=models.CharField(max_length=13)
    national_id=models.CharField(max_length=40)
    gra_tin=models.CharField(max_length=40)
    
    def __str__(self):
        return self.last_name

class Payment(models.Model):
    employee_code=models.ForeignKey(Employee,on_delete=DO_NOTHING)
    national_id=models.CharField(max_length=30)
    ghloxid=models.CharField(max_length=30)
    
    TRANSTYPES=(
        ('Earning','earning'),
        ('Deduction','deduction')
    )
    transtype=models.CharField(max_length=80,choices=TRANSTYPES)
    transname=models.CharField(max_length=120)
    amount=models.DecimalField(decimal_places=2,max_digits=8)

    def __str__(self) -> str:
        return self.employee_code + self.transtype +self.transname+self.amount


class Affordability(models.Model):
    employee_number=models.ForeignKey(Employee,on_delete=DO_NOTHING)
    staff_id=models.CharField(max_length=20)
    name=models.CharField(max_length=120)
    ssf_number=models.CharField(max_length=13)
    monthly_afford=models.DecimalField(decimal_places=2,max_digits=8)
    running_afford=models.DecimalField(decimal_places=2,max_digits=8)
    period=models.CharField(max_length=20)

    def __str__(self) -> str:
        return self.name +': '+ self.period+'-'+self.monthly_afford+'-'+self.running_afford

class ActivityLog(models.Model):
    user_id=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    username=models.CharField(max_length=120)
    module=models.CharField(max_length=100)
    remote_addr=models.CharField(max_length=40)
    request_uri=models.CharField(max_length=255)
    agent=models.CharField(max_length=255)
    activity=models.CharField(max_length=200)
    created=models.DateTimeField(auto_created=True)

    def __str__(self):
        return self.user_id + self.created +self.activity

class LoginAttempts(models.Model):
    ip_address=models.CharField(max_length=39,default='0')
    timestamp=models.DateTimeField(blank=True)
    attempts=models.SmallIntegerField()

    def __str__(self):
        return self.ip_address + self.timestamp + self.attempts

class Mandate(models.Model):
    code=models.CharField(max_length=20)
    employee_code=models.ForeignKey(Employee,on_delete=DO_NOTHING)
    company=models.ForeignKey(Company,on_delete=DO_NOTHING)
    status=models.CharField(max_length=30)
    date=models.DateTimeField(auto_now=True)
    expiredate=models.DateTimeField()
    verified=models.BooleanField()

    def __str__(self):
        return self.code + self.employee_code +self.status + str(self.date)
