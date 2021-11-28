from django.db.models import query
from rest_framework import generics,viewsets
from .models import Employee,ActivityLog,LoginAttempts,CompanyBranch,Company,Affordability,Payment,Mandate,Bank,BankBranch,Element,ElementGroup,ElementCategory
from django.contrib.auth import get_user_model
from .serilizers import MandateSerializer,ActivityLogSerializer, AffordabilitySerializer, CompanyBranchSerializer, CompanySerializers, EmployeeSerializer, LoginAttemptsSerializer, PaymentSerializer, UserSerializer,BankSerializer,BankBranchSerializer,ElementSerializer,ElementGroupSerializer,ElementCategorySerializer


# Create your views here.
class CompanyViewSet(viewsets.ModelViewSet):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers

class CompanyBranchViewSet(viewsets.ModelViewSet):
    queryset=CompanyBranch.objects.all()
    serializer_class=CompanyBranchSerializer


class AffordabilityViewSet(viewsets.ModelViewSet):
    queryset=Affordability.objects.all()
    serializer_class=AffordabilitySerializer



class PaymentViewSet(viewsets.ModelViewSet):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer


class MandateViewSet(viewsets.ModelViewSet):
    queryset=Mandate.objects.all()
    serializer_class=MandateSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset= Employee.objects.all()
    serializer_class=EmployeeSerializer

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
    
