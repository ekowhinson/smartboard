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
    status=models.BooleanField(default=False)
    date_created=models.DateTimeField(auto_now=True)
    contact_number1=models.CharField(max_length=30)
    contact_number2=models.CharField(max_length=30)
    ceo_number=models.CharField(max_length=30)
    ceo_name=models.CharField(max_length=120)
    contact_person=models.CharField(max_length=120)
    address=models.CharField(max_length=150)
    postal_address=models.CharField(max_length=150)
    landmark=models.CharField(max_length=200)
    authorization_status=BooleanField(default=False)
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
    middle_name=models.CharField(max_length=80, blank=True)
    last_name=models.CharField(max_length=80)
    company=models.ForeignKey(Company,on_delete=DO_NOTHING)
    company_branch=models.ForeignKey(CompanyBranch,on_delete=DO_NOTHING)
    ssnit_number=models.CharField(max_length=13)
    national_id=models.CharField(max_length=40)
    gra_tin=models.CharField(max_length=40)
    username=models.CharField(max_length=50,null=True,blank=True)
    email=models.EmailField(null=True,blank=True)
    mobile_no=models.CharField(max_length=20,null=True,blank=True)
    password=models.CharField(max_length=200,null=True,blank=True)
    address=models.CharField(max_length=200,null=True,blank=True)
    is_active=models.IntegerField(default=1)
    is_verify=models.IntegerField(default=0)
    token=models.CharField(max_length=200,null=True,blank=True)
    password_reset_code=models.CharField(max_length=200,null=True,blank=True)
    last_ip=models.CharField(max_length=30,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at=models.DateTimeField(auto_now=True,blank=True,null=True)
        
    def __str__(self):
        return self.last_name

class Payment(models.Model):
    employee_code=models.ForeignKey(Employee,on_delete=DO_NOTHING)
    national_id=models.CharField(max_length=30)
    ghloxid=models.CharField(max_length=30)
    
    TRANSTYPES=(
        ('Earning','earning'),
        ('Deduction','deduction'),
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

class Bank(models.Model):
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=150)
    short_name=models.CharField(max_length=50)
    status=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class BankBranch(models.Model):
    bankCode=models.ForeignKey(Bank,on_delete=models.CASCADE)
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=150)
    
    def __str__(self):
        return self.name

class Element(models.Model):
    code=models.CharField(max_length=50)
    clgcode=models.CharField(max_length=50)
    catcode=models.CharField(max_length=50)
    amount=models.DecimalField(decimal_places=2,max_digits=8)
    status=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)
    real=models.CharField(max_length=50)
    typeid=models.CharField(max_length=50)
    emap=models.CharField(max_length=50)
    companyid=models.ForeignKey(Company,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.code

class ElementCategory(models.Model):
    code=models.CharField(max_length=50)
    platform=models.CharField(max_length=50)
    name=models.CharField(max_length=150)
    description=models.CharField(max_length=150)
    apply_affordability=models.BooleanField(default=False)
    status=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class ElementGroup(models.Model):
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=150)
    rate=models.DecimalField(decimal_places=2,max_digits=8)
    category=models.CharField(max_length=50)
    bank_name=models.ForeignKey(Bank,on_delete=models.DO_NOTHING)
    bank_branch=models.ForeignKey(BankBranch,on_delete=models.DO_NOTHING)
    acc_no=models.CharField(max_length=80)
    status=models.BooleanField(default=False)
    elementcreated=models.BooleanField(default=False)
    date=models.DateTimeField(auto_now_add=True)
   
    def __str__(self):
        return self.name
