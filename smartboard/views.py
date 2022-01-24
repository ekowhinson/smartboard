from django.shortcuts import render
from django.db.models import query
from rest_framework import generics,viewsets
from . import models as smodels
from . import serializers as sbserializers
# Create your views here.

class SchoolViewSet(viewsets.ModelViewSet):
    queryset=smodels.School.objects.all()
    serializer_class=sbserializers.SchoolSerializer
    filterset_fields=['name']

class AcademicSettingsViewSet(viewsets.ModelViewSet):
    queryset=smodels.AcademicSettings.objects.all()
    serializer_class=sbserializers.AcademicSettingsSerializer
    filterset_fields=['school']

class AcademicYearViewSet(viewsets.ModelViewSet):
    queryset=smodels.AcademicYear.objects.all()
    serializer_class=sbserializers.AcademicYearSerializer
    filterset_fields=['school']

class AccountRoleViewSet(viewsets.ModelViewSet):
    queryset=smodels.AccountRole.objects.all()
    serializer_class=sbserializers.AccountRoleSerializer
    filterset_fields=['school']

class AdminViewSet(viewsets.ModelViewSet):
    queryset=smodels.Admin.objects.all()
    serializer_class=sbserializers.AdminSerializer
    filterset_fields=['school']