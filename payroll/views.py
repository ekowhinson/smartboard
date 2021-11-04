from django.db.models import query
from rest_framework import generics
from .models import Employee,ActivityLog,LoginAttempts,CompanyBranch,Company,Affordability,Payment,Mandate
from django.contrib.auth.models import User
from .serilizers import MandateSerializer,ActivityLogSerializer, AffordabilitySerializer, CompanyBranchSerializer, CompanySerializers, EmployeeSerializer, LoginAttemptsSerializer, PaymentSerializer, UserSerializer


# Create your views here.
class CompanyList(generics.ListCreateAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers

class CompanyDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Company.objects.all()
    serializer_class=CompanySerializers

class CompanyBranchList(generics.ListCreateAPIView):
    queryset=CompanyBranch.objects.all()
    serializer_class=CompanyBranchSerializer

class CompanyBranchDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=CompanyBranch.objects.all()
    serializer_class=CompanyBranchSerializer

class AffordabilityList(generics.ListCreateAPIView):
    queryset=Affordability.objects.all()
    serializer_class=AffordabilitySerializer

class AffordabilityDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Affordability.objects.all()
    serializer_class=AffordabilitySerializer

class PaymentList(generics.ListCreateAPIView):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer


class PaymentDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Payment.objects.all()
    serializer_class=PaymentSerializer    

class MandateList(generics.ListCreateAPIView):
    queryset=Mandate.objects.all()
    serializer_class=MandateSerializer

class MandateDetails(generics.RetrieveUpdateDestroyAPIView):
    queryset=Mandate.objects.all()
    serializer_class=MandateSerializer

class EmployeeList(generics.ListCreateAPIView):
    #permission_classes=(permissions.IsAuthenticated,)
    queryset= Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    #permission_classes=(permissions.IsAuthenticated,)
    queryset= Employee.objects.all()
    serializer_class=EmployeeSerializer

class UserList(generics.ListAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerializer


class ActivityLogList(generics.ListCreateAPIView):
    queryset=ActivityLog.objects.all()
    serializer_class=ActivityLogSerializer

class LoginAttemptsList(generics.ListCreateAPIView):
    queryset=LoginAttempts.objects.all()
    serializer_class=LoginAttemptsSerializer
