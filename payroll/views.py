from django.db.models import query
from rest_framework import generics
from .models import Employee,ActivityLog,LoginAttempts
from django.contrib.auth.models import User
from .serilizers import ActivityLogSerializer, EmployeeSerializer, LoginAttemptsSerializer, UserSerializer

# Create your views here.
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
