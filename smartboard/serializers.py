from django.db.models import fields
from rest_framework import serializers
from . import models as smbmodels

class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.School
        fields='__all__'

class AcademicSettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.AcademicSettings
        fields='__all__'

class AcademicYearSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.AcademicYear
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

class BillingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.BillingCategory
        fields='__all__'

class DormitorySerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Dormitory
        fields='__all__'

class TeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Teacher
        fields='__all__'

class ParentSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Parent
        fields='__all__'

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Level
        fields='__all__'

class ClassesSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Classes
        fields='__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Student
        fields='__all__'