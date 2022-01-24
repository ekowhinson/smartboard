from django.shortcuts import render
from django.db.models import query
from rest_framework import generics,viewsets
from . import models as smodels
from . import serializers as sbserializers
# Create your views here.

class SchoolViewSet(viewsets.ModelViewSet):
    queryset=smodels.School.objects.all()
    serizer_class=sbserializers.SchoolSerializer
    filterset_fields=['name']