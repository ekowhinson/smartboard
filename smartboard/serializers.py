from django.db.models import fields
from rest_framework import serializers
from . import models as smbmodels

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.School
        fields='__all__'