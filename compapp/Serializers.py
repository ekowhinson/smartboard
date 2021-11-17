from rest_framework import serializers
from .models import CiAdmin
from django.contrib.auth import get_user_model

class CiAdminSerializer(serializers.ModelSerializer):
    class Meta:
        fields='__all__'
        model=CiAdmin