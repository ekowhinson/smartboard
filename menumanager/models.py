from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE, SET_NULL,DO_NOTHING

# Create your models here.

#CustomUser=get_user_model()

class MenuGroup(models.Model):
    code=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    description=models.CharField(max_length=200,null=True,blank=True)
    ENABLE='1'
    DISABLE='0'
    STATUS=(
        (DISABLE,'Disable'),
        (ENABLE,'Enable'),
    )
    status=models.CharField(max_length=20,choices=STATUS,default=ENABLE)
    date=models.DateTimeField(auto_created=True,auto_now=True)
    
    def __str__(self):
	    return self.name  

class MenuSubGroup(models.Model):
    menugpcode=models.CharField(max_length=50)
    code=models.CharField(max_length=50)
    name=models.CharField(max_length=100)
    namespace=models.CharField(max_length=255)
    icons=models.CharField(max_length=150)
    DISABLE='0'
    ENABLE='1'
    STATUS=(
        (DISABLE,'Disable'),
        (ENABLE,'Enable') 
    )
    status=models.CharField(max_length=20,choices=STATUS,default=ENABLE)
    date=models.DateTimeField(auto_created=True,auto_now=True)    
    def __str__(self):
        return self.name

class MenuSubGroupDetail(models.Model):
    menugpcode=models.CharField(max_length=50,blank=True,null=True)
    menucatcode=models.CharField(max_length=50,blank=True,null=True)
    code=models.CharField(max_length=50,blank=True,null=True)
    icons=models.CharField(max_length=150,blank=True,null=True)
    name=models.CharField(max_length=100,blank=True,null=True)
    namespace=models.CharField(max_length=255,blank=True,null=True)
    imageuniname=models.CharField(max_length=150,blank=True,null=True)
    STATUS=(
        ('0','Disable'),
        ('1','Enable')
    )
    status=models.CharField(max_length=20,choices=STATUS,default='1')
    NCI=(
        ('0','No notification icon'),
        ('1','Notification icon'),
    )
    notification=models.CharField(max_length=20,choices=NCI,default='0')
    SB=(
        ('0','Off'),
        ('1','On'),
    )
    sidebar=models.CharField(max_length=20,choices=SB,default='1')
    dashboard=models.CharField(max_length=20,choices=SB,default='1')
    windview=models.CharField(max_length=20,choices=SB,default='0')
    windviewgeneralreport=models.CharField(max_length=20,choices=SB,null=True,blank=True)
    windviewfinancialreport=models.CharField(max_length=20,choices=SB,null=True,blank=True)
    windviewstatisticalreport=models.CharField(max_length=20,choices=SB,null=True,blank=True)
    ACR=(
        ('1','General User'),
        ('2','Administrator Access Right. (Manage Settlement Account) Reserved for Facility administrators'),
    )
    admin_accessright=models.CharField(max_length=250,choices=ACR,default='1')
    date=models.DateTimeField(auto_created=True,auto_now=True)
    targeted=models.CharField(max_length=255,null=True,blank=True)
    viewer=models.CharField(max_length=255,null=True,blank=True)

    def __str__(self):
        return self.name

class MenuSubUsers(models.Model):
    usruserid=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    menudetcode=models.CharField(max_length=50,null=True,blank=True)
    STATUS=(
        ('0','Revoked'),
        ('1','Granted'),
    ) 
    status=models.CharField(max_length=50,choices=STATUS,default='1')
    addedby=models.CharField(max_length=50,null=True,blank=True)
    date=models.DateTimeField(auto_now=True,auto_created=True)

    def __str__(self):
        return self.usruseri+' '+self.menudetcode
   
class DaUsers(models.Model):
    code=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    brchid=models.CharField(max_length=50)
    surname=models.CharField(max_length=100)
    othernames=models.CharField(max_length=100)
    password=models.CharField(max_length=400)
    username=models.CharField(max_length=50)
    startdate=models.DateField(auto_now=True,auto_created=True)
    emergencyphone=models.CharField(max_length=255,null=True,blank=True)
    phoneno=models.CharField(max_length=100,null=True,blank=True)
    LEVEL=(
        ('1','administrator'),
        ('2','operator'),
        ('3','Manager'),
    )
    level=models.CharField(max_length=50,choices=LEVEL,null=True,blank=True,default='2')
    email=models.CharField(max_length=255,null=True,blank=True)
    STATUS=(
        ('-1','Deleted'),
        ('0','Disabled'),
        ('1','Enabled'),
    )
    status=models.CharField(max_length=50,choices=STATUS,default='1')
    actorid=models.IntegerField(null=True,blank=True)
    date=models.DateTimeField(auto_now=True,auto_created=True)

    def __str__(self):
        return self.surname+' '+ self.othernames

class UsersPermission(models.Model):
    usruserid=models.ForeignKey(User,on_delete=models.DO_NOTHING)
    menudetcode=models.CharField(max_length=50)
    STATUS=(
        ('0','Revoked'),
        ('1','Granted'), 
    )
    status=models.CharField(max_length=50,choices=STATUS,default='0')
    addedby=models.CharField(max_length=50,null=True,blank=True)
    date=models.DateTimeField(auto_now=True,auto_created=True)

    def __str__(self):
        return self.usruserid+' '+self.menudetcode


