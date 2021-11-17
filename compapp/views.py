from django.shortcuts import render
from rest_framework import generics,viewsets
from .models import CiAdmin,CiAdminRoles
from .Serializers import CiAdminSerializer,CiAdminRolesSerializer

# Create your views here.
class CiAdminViewSet(viewsets.ModelViewSet):
    queryset=CiAdmin.objects.all()
    serializer_class=CiAdminSerializer
    filterset_fields=['username','is_active']

class CiAdminRolesViewSet(viewsets.ModelViewset):
    queryset=CiAdminRoles.objects.all()
    serializer_class=CiAdminRolesSerializer