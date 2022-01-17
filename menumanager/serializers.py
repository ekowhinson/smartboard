from django.db.models import fields
from rest_framework import serializers
from .models import DaUsers, EventLog, EventType,MenuGroup,MenuSubGroup,MenuSubGroupDetail,MenuSubUsers,UsersPermission,MenuUserElement

class MenuUserElementSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=MenuUserElement

class MenuGroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','code','name','description','date',)
        model=MenuGroup

class MenuSubGroupSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','menugpcode','code','name','namespace','icons','status','date',)
        model=MenuSubGroup

class MenuSubGroupDetailSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','menugpcode','menucatcode','code','icons','name','namespace','imageuniname','status','notification','sidebar','dashboard','windview','windviewgeneralreport','windviewfinancialreport','windviewstatisticalreport','admin_accessright','date','targeted','viewer',)
        model=MenuSubGroupDetail

class MenuSubUsersSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','usruserid','menudetcode','status','addedby','date',)
        model=MenuSubUsers

class DaUsersSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','code','brchid','surname','backenduser','othernames','password','username','startdate','emergencyphone','companyid','phoneno','level','email','status','actorid','date')
        model=DaUsers

class UsersPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        fields=('id','usruserid','menudetcode','status','addedby','date',)
        model=UsersPermission

class EventLogSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=EventLog

class EventTypeSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=EventType
