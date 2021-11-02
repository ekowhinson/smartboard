from rest_framework import serializers
from .models import Employee,UserGroups,ActivityLog,LoginAttempts
from django.contrib.auth.models import User

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        fields=('id','code','first_name','middle_name','last_name','company','company_branch','ssnit_number','gra_tin','national_id',)
        model=Employee

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('username','password')
        model=User
class UserGroupsSerializer(serializers.ModelSerializer):
    fields=('id','user_id','group_id',)
    model=UserGroups

class ActivityLogSerializer(serializers.ModelSerializer):
    fields=('id','description','created','user',)
    model=ActivityLog

class LoginAttemptsSerializer(serializers.ModelSerializer):
    fields=('id','ip_address','timestamp')