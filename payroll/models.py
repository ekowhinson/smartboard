from ast import increment_lineno
from sys import dont_write_bytecode
from types import MemberDescriptorType
#from menumanager import models as cmodels
from django.db import models
from django.contrib.auth.models import User
from django.db.models.base import Model, ModelStateFieldsCacheDescriptor
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields import BooleanField, CharField
from django.db.models.fields.related import ForeignKey

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
    alias=models.CharField(max_length=50)
    
    def __str__(self):
        return self.code + ': ' +self.name

class CompanyBranch(models.Model):
    company=models.ForeignKey(Company,on_delete=DO_NOTHING)
    branch_name=models.CharField(max_length=120)
    date=models.DateField(auto_now=True)

    def __str__(self):
        return str(self.company) +', '+ self.branch_name

class CompanySettings(models.Model):
    companyid=models.ForeignKey(Company,on_delete=models.DO_NOTHING)
    address=models.CharField(max_length=150)
    Phone=models.IntegerField()
    email=models.EmailField()
    logo=models.CharField(max_length=100)
    
    def __str__(self) -> str:
        return f'{self.companyid} {self.address}'

class CompanyRate(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=100)
    rate=models.DecimalField(max_digits=8,decimal_places=2)
    status=models.IntegerField()


class Employee(models.Model):
    code=models.CharField(max_length=20,unique=True)
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
    reason=models.CharField(max_length=200,blank=True,null=True)
    last_ip=models.CharField(max_length=30,null=True,blank=True)
    created_at=models.DateTimeField(blank=True,null=True)
    updated_at=models.DateTimeField(blank=True,null=True)
        
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
    balance=models.DecimalField(decimal_places=2,max_digits=8,blank=True,null=True)
    comp_id=models.ForeignKey(Company,on_delete=CASCADE)
    
    def __str__(self):
        return f'{self.employee_code} {self.transtype} {self.transname} {self.amount}'


class Affordability(models.Model):
    employee_number=models.ForeignKey(Employee,on_delete=DO_NOTHING)
    staff_id=models.CharField(max_length=20)
    name=models.CharField(max_length=120)
    ssf_number=models.CharField(max_length=13)
    monthly_afford=models.DecimalField(decimal_places=2,max_digits=8)
    running_afford=models.DecimalField(decimal_places=2,max_digits=8)
    period=models.CharField(max_length=20)
    compid=models.ForeignKey(Company,on_delete=models.DO_NOTHING)
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
    compid=models.ForeignKey(Company,on_delete=models.DO_NOTHING)
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
    name=models.CharField(max_length=150)
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

class Rejections(models.Model):
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=150)
    description=models.CharField(max_length=250)
    compid=models.ForeignKey(Company,on_delete=models.DO_NOTHING)
    status=models.BooleanField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} {self.description}'

class Product(models.Model):
    name=models.CharField(max_length=50)
    compid=models.ForeignKey(Company,on_delete=models.DO_NOTHING)
    elementcode=models.ForeignKey(Element,on_delete=models.DO_NOTHING)
    authorid=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    duration=models.PositiveIntegerField()
    status=models.BooleanField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name}'

class Positions(models.Model):
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=150)
    compid=models.ForeignKey(Company,on_delete=models.CASCADE)

class AuthorityNote(models.Model):
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=150)
    compid=models.ForeignKey(Company,on_delete=models.DO_NOTHING)
    rate=models.DecimalField(decimal_places=2,max_digits=7)
    category=models.ForeignKey(ElementCategory,on_delete=models.DO_NOTHING)
    bank=models.ForeignKey(Bank,on_delete=models.DO_NOTHING)
    bank_branch=models.ForeignKey(BankBranch,on_delete=models.DO_NOTHING)
    acc_no=models.CharField(max_length=50)
    status=models.BooleanField()
    date=models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.name}'

class Transaction(models.Model):
    loanAdvNo=models.CharField(max_length=50)
    authority_note=models.ForeignKey(AuthorityNote,on_delete=models.DO_NOTHING)
    element_code=models.ForeignKey(Element,on_delete=DO_NOTHING)
    description=models.CharField(max_length=100)
    compid=models.ForeignKey(Company,on_delete=models.DO_NOTHING)
    employee=models.ForeignKey(Employee,on_delete=models.DO_NOTHING)
    employee_name=models.CharField(blank=True,max_length=150,null=True)
    total_repayment=models.DecimalField(decimal_places=2,max_digits=8,null=True)
    principal=models.DecimalField(blank=True,max_digits=8,decimal_places=2,null=True)
    monthly_pay=models.DecimalField(blank=True,max_digits=8,decimal_places=2,null=True)
    duration=models.IntegerField(blank=True,null=True)
    affordability=models.DecimalField(null=True,blank=True,max_digits=8,decimal_places=2)
    application_date=models.DateField(blank=True,null=True)
    start_date=models.DateField(blank=True,null=True)
    transaction_type=models.CharField(max_length=80,choices=(('loan','Loan'),('insurance','Insurance')),blank=True,null=True)
    authorization_satus=models.BooleanField(blank=True,null=True)
    authorization_date=models.DateField(blank=True,null=True)
    
    def __str__(self) -> str:
        return f'{self.description}'

class UserElement(models.Model):
    userid=models.ForeignKey(User,on_delete=models.CASCADE)
    element_code=models.ForeignKey(Element,on_delete=models.DO_NOTHING)
    companyid=models.ForeignKey(Company,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return f'{self.userid} {self.element_code} {self.companyid}'

class TesterTable(models.Model):
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=100)
