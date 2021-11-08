from django.shortcuts import render
from .models import MenuGroup
from .serializers import MenuGroupSerializer
from rest_framework import viewsets

# Create your views here.
class MenuGropuViewSet(viewsets.ModelViewSet):
    queryset= MenuGroup.objects.all()
    serializer_class=MenuGroupSerializer