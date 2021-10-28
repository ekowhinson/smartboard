from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):

    class Meta:
        fields=('id','code','first_name','middle_name','last_name',)
        model=Employee