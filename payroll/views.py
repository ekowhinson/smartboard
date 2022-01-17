from django.db.models import query
from rest_framework import generics,viewsets
from .models import CompanyRate,CompanySettings,Employee,ActivityLog,LoginAttempts,CompanyBranch,Company,Affordability,Payment,Mandate,Bank,BankBranch,Element,ElementGroup,ElementCategory,Rejections,Product, TesterTable,UserElement,Transaction,Positions,AuthorityNote
from django.contrib.auth import get_user_model
from .serilizers import CompanyRateSerializer,CompanySettingsSerializer,MandateSerializer,ActivityLogSerializer, AffordabilitySerializer, CompanyBranchSerializer, CompanySerializers, EmployeeSerializer, LoginAttemptsSerializer, PaymentSerializer, PositionSerializer, TestTableSerializer, UserSerializer,BankSerializer,BankBranchSerializer,ElementSerializer,ElementGroupSerializer,ElementCategorySerializer,RejectionSerializer,ProductSerializer,UserElementSerializer,AuthorityNoteSerializer,TransactionSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Create your views here.

class RejectionViewSet(viewsets.ModelViewSet):
    queryset=Rejections.objects.all()
    serializer_class=RejectionSerializer
    filterset_fields=['compid']

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer
    filterset_fields=['compid']

class PositionViewSet(viewsets.ModelViewSet):
    queryset=Positions.objects.all()
    serializer_class=PositionSerializer
    filterset_fields=['compid']

class AuthorityNoteViewSet(viewsets.ModelViewSet):
    queryset=AuthorityNote.objects.all()
    serializer_class=AuthorityNoteSerializer
    filterset_fields=['compid','code']

class UserElementViewSet(viewsets.ModelViewSet):
    queryset=UserElement.objects.all()
    serializer_class=UserElementSerializer
    filterset_fields=['companyid']

class TransactionViewSet(viewsets.ModelViewSet):
    queryset=Transaction.objects.all()
    serializer_class=TransactionSerializer
    filterset_fields=['compid','employee']

class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers
    filterset_fields=['company_type']
class CompanyBranchViewSet(viewsets.ModelViewSet):
    queryset=CompanyBranch.objects.all()
    serializer_class=CompanyBranchSerializer
    filterset_fields=['company']

class AffordabilityViewSet(viewsets.ModelViewSet):
    queryset=Affordability.objects.all()
    serializer_class=AffordabilitySerializer



class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer


class MandateViewSet(viewsets.ModelViewSet):
    queryset=Mandate.objects.all()
    serializer_class=MandateSerializer
    filterset_fields=['employee_code','code']

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class=EmployeeSerializer
    filterset_fields=['company','code','is_active','is_verify']

class UserViewSet(viewsets.ModelViewSet):
    queryset=get_user_model().objects.all()
    serializer_class=UserSerializer
    filterset_fields=['username']

class ActivityLogList(generics.ListCreateAPIView):
    queryset=ActivityLog.objects.all()
    serializer_class=ActivityLogSerializer

class LoginAttemptsList(generics.ListCreateAPIView):
    queryset=LoginAttempts.objects.all()
    serializer_class=LoginAttemptsSerializer

class BankViewSet(viewsets.ModelViewSet):
    queryset=Bank.objects.all()
    serializer_class=BankSerializer
    filterset_fields=['code']

class BankBranchViewSet(viewsets.ModelViewSet):
    queryset=BankBranch.objects.all()
    serializer_class=BankBranchSerializer
    filterset_fields=['bankCode','code']

class ElementViewSet(viewsets.ModelViewSet):
    queryset=Element.objects.all()
    serializer_class=ElementSerializer
    filterset_fields=['companyid']

class ElementCategoryViewSet(viewsets.ModelViewSet):
    queryset=ElementCategory.objects.all()
    serializer_class=ElementCategorySerializer
    
class ElementGroupViewSet(viewsets.ModelViewSet):
    queryset=ElementGroup.objects.all()
    serializer_class=ElementGroupSerializer
    
class TesterTableViewSet(viewsets.ModelViewSet):
    queryset=TesterTable.objects.all()
    serializer_class=TestTableSerializer

class CompanySettingsView(viewsets.ModelViewSet):
    queryset=CompanySettings.objects.all()
    serializer_class=CompanySettingsSerializer

class companyRateView(viewsets.ModelViewSet):
    queryset=CompanyRate.objects.all()
    serializer_class=CompanyRateSerializer
    