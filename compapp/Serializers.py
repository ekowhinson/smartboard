from rest_framework import serializers
from .models import ModuleAccess,CiAdmin,CiAdminRoles,Module
from django.contrib.auth import get_user_model

class CiAdminSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=CiAdmin

class CiAdminRolesSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=CiAdminRoles

class ModuleSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=Module

class ModuleAccessSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=ModuleAccess