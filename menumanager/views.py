from django.shortcuts import render
from .models import MenuGroup,MenuSubGroup,MenuSubGroupDetail,MenuSubUsers,DaUsers
from .serializers import MenuSubUsersSerializer ,MenuGroupSerializer,MenuSubGroupDetailSerializer,MenuSubGroupSerializer,DaUsersSerializer
from rest_framework import viewsets

# Create your views here.
class MenuGroupViewSet(viewsets.ModelViewSet):
    queryset= MenuGroup.objects.all()
    serializer_class=MenuGroupSerializer

class MenuSubGroupViewSet(viewsets.ModelViewSet):
    queryset=MenuSubGroup.objects.all()
    serializer_class=MenuSubGroupSerializer

class MenuSubGroupDetailViewSet(viewsets.ModelViewSet):
    queryset=MenuSubGroupDetail.objects.all()
    serializer_class=MenuSubGroupDetailSerializer

class MenuSubUsersViewSet(viewsets.ModelViewSet):
    queryset=MenuSubUsers.objects.all()
    serializer_class=MenuSubUsersSerializer

class DaUsersViewSet(viewsets.ModelViewSet):
    queryset=DaUsers.objects.all()
    serializer_class=DaUsersSerializer
