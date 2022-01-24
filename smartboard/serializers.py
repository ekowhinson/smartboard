from django.db.models import fields
from rest_framework import serializers
from . import models as smbmodels

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.School
        fields='__all__'

class AcademicSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        models=smbmodels.AcademicSettings
        fields='__all__'

class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        models=smbmodels.AcademicYear
        fields='__all__'

class AccountRoleSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.AccountRole
        fields='__all__'

class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Admin
        fields='__all__'

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Attendance
        fields='__all__'