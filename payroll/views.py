from django.db.models import query
from rest_framework import generics,permissions
from .models import Employee
from django.contrib.auth.models import User
from .serilizers import EmployeeSerializer,UserSerializer

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