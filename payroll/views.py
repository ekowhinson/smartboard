from rest_framework import generics
from .models import Employee
from .serilizers import EmployeeSerializer

# Create your views here.
class EmployeeList(generics.ListCreateAPIView):
    queryset= Employee.objects.all()
    serializer_class=EmployeeSerializer

class EmployeeDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset= Employee.objects.all()
    serializer_class=EmployeeSerializer