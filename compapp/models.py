from django.db import models
from django.contrib.auth.models import User
from payroll.models import Company
# Create your models here.
class CiAdmin(models.Model):
    admin_role_id=models.IntegerField()
    sysuserid=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    username=models.CharField(max_length=100)
    firstname=models.CharField(max_length=200)
    lastname=models.CharField(max_length=200)
    email=models.EmailField()
    mobile_no=models.CharField(max_length=20)
    image=models.CharField(max_length=300)
    password=models.CharField(max_length=255)
    last_login=models.DateTimeField()
    is_verify=models.IntegerField(default=1)
    is_admin=models.IntegerField(default=1)
    is_active=models.IntegerField(default=0)
    is_super=models.IntegerField(default=0)
    token=models.CharField(max_length=255)
    password_reset_code=models.CharField(max_length=255,null=True,blank=True)
    last_ip=models.CharField(max_length=200,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    company_id=models.ForeignKey(Company,on_delete=models.DO_NOTHING)

    
    def __str__(self):
        return self.username

