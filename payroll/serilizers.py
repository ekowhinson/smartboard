from rest_framework import serializers
from .models import Employee,ActivityLog,LoginAttempts
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        fields=('id','code','first_name','middle_name','last_name','company','company_branch','ssnit_number','gra_tin','national_id',)
        model=Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('username','password','first_name','last_name','groups','user_permissions',)
        model=User

class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','description','created','username',)
        model=ActivityLog

class LoginAttemptsSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','ip_address','timestamp','attempts',)
        model=LoginAttempts