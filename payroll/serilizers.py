from django.db.models import fields
from rest_framework import serializers
from .models import AffordabilityFormular, BankBranch,Bank, CompanyRate, CompanySettings,Employee,ActivityLog,LoginAttempts,CompanyBranch,Company,Affordability,Payment,Mandate,Element,ElementCategory,ElementGroup,Product, TesterTable,Transaction,Positions,Rejections,AuthorityNote,UserElement
from django.contrib.auth import get_user_model


class CompanySettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanySettings
        fields='__all__'

class CompanyRateSerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyRate
        fields='__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Product

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Transaction


class PositionSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Positions

class RejectionSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Rejections

class AuthorityNoteSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=AuthorityNote

class UserElementSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=UserElement
        
class CompanySerializers(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Company

class CompanyBranchSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=CompanyBranch

class PaymentSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Payment

class AffordabilitySerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Affordability

class MandateSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Mandate

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        fields='__all__'
        model=Employee


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','username','password','first_name','last_name','groups','user_permissions',)
        model=get_user_model()

class ActivityLogSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=ActivityLog

class LoginAttemptsSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=LoginAttempts

class BankSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Bank

class BankBranchSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=BankBranch

class ElementSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Element

class ElementCategorySerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=ElementCategory

class ElementGroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=ElementGroup

class TestTableSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=TesterTable

class AffordabilityFormSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=AffordabilityFormular