from django.db.models.query import QuerySet
from django.shortcuts import render
from .models import UsersPermission ,MenuGroup,MenuSubGroup,MenuSubGroupDetail,MenuSubUsers,DaUsers
from .serializers import UsersPermissionSerializer ,MenuSubUsersSerializer ,MenuGroupSerializer,MenuSubGroupDetailSerializer,MenuSubGroupSerializer,DaUsersSerializer
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
    filterset_fields=['usruserid']
    
class MenuSubUsersDelete(viewsets.ViewSet):

    def destroy(self, request,usrid):
        subusers = MenuSubUsers.objects.filter(usruserid=usrid)
        if subusers:
            subusers.delete()


class DaUsersViewSet(viewsets.ModelViewSet):
    queryset=DaUsers.objects.all()
    serializer_class=DaUsersSerializer
    filterset_fields=['username','companyid']

class UsersPermissionViewSet(viewsets.ModelViewSet):
    queryset=UsersPermission.objects.all()
    serializer_class=UsersPermissionSerializer


    
