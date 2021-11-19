from django.db.models import fields
from rest_framework import serializers
from .models import BankBranch,Bank,Employee,ActivityLog,LoginAttempts,CompanyBranch,Company,Affordability,Payment,Mandate,Element,ElementCategory,ElementGroup
from django.contrib.auth import get_user_model

class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        fields=('id','code','name','email','contact_number','status','date_created','contact_number1','contact_number2','ceo_number','ceo_name','contact_person','address','postal_address','landmark','authorization_status','authorized_by',)
        model=Company

class CompanyBranchSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','company','branch_name','date')
        model=CompanyBranch

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','employee_code','national_id','ghloxid','transtype','transname','amount',)
        model=Payment

class AffordabilitySerializer(serializers.ModelSerializer):
    class Meta:
        fields=('employee_number','staff_id','name','ssf_number','monthly_afford','running_afford','period')
        model=Affordability

class MandateSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('code','employee_code','company','status','date','expiredate','verified',)
        model=Mandate

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        fields=('id','code','first_name','middle_name','last_name','company','company_branch','ssnit_number','gra_tin','national_id',)
        model=Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('username','password','first_name','last_name','groups','user_permissions',)
        model=get_user_model()

class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','activity','user_id','username','module','request_uri','agent','created')
        model=ActivityLog

class LoginAttemptsSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','ip_address','timestamp','attempts',)
        model=LoginAttempts

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','code','name','short_name','status','date')
        model=Bank

class BankBranchSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','bankCode','code','name')
        model=BankBranch

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Element

class ElementCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','code','platform','name','description','apply_affordability','status','date')
        model=ElementCategory

class ElementGroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','code','name','rate','category','bank_name','bank_branch','acc_no','status','elementcreated','date')
        model=ElementGroup

