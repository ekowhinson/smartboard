from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import ModuleAccess,CiAdmin,CiAdminRoles,Module
from .Serializers import ModuleAccessSerializer,ModuleSerializer,CiAdminSerializer,CiAdminRolesSerializer

# Create your views here.
class CiAdminViewSet(viewsets.ModelViewSet):
    queryset=CiAdmin.objects.all()
    serializer_class=CiAdminSerializer
    filterset_fields=['username','is_active']

class CiAdminRolesViewSet(viewsets.ModelViewSet):
    queryset=CiAdminRoles.objects.all()
    serializer_class=CiAdminRolesSerializer
    filterset_fields=['compid','status']

class ModuleViewSet(viewsets.ModelViewSet):
    queryset=Module.objects.all()
    serializer_class=ModuleSerializer

class ModuleAccessViewSet(viewsets.ModelViewSet):
    queryset=ModuleAccess.objects.all()
    serializer_class=ModuleAccessSerializer
    