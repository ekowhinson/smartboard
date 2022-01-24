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

class BillingCategoryViewSet(viewsets.ModelViewSet):
    queryset=smodels.BillingCategory.objects.all()
    serializer_class=sbserializers.BillingCategorySerializer
    filterset_fields=['school']

class DormitoryViewSet(viewsets.ModelViewSet):
    queryset=smodels.Dormitory.objects.all()
    serializer_class=sbserializers.DormitorySerializer
    filterset_fields=['school']

class TeacherViewSet(viewsets.ModelViewSet):
    queryset=smodels.Teacher.objects.all()
    serializer_class=sbserializers.TeacherSerializer
    filterset_fields=['school']

class ParentViewSet(viewsets.ModelViewSet):
    queryset=smodels.Parent.objects.all()
    serializer_class=sbserializers.ParentSerializer
    filterset_fields=['school']

class LevelViewSet(viewsets.ModelViewSet):
    queryset=smodels.Level.objects.all()
    serializer_class=sbserializers.LevelSerializer
    filterset_fields= ['school']

class ClassesViewSet(viewsets.ModelViewSet):
    queryset=smodels.Classes.objects.all()
    serializer_class=sbserializers.ClassesSerializer
    filterset_fields=['school']

class StudentViewSet(viewsets.ModelViewSet):
    queryset=smodels.Student.objects.all()
    serializer_class=sbserializers.StudentSerializer
    filterset_fields=['school']

class ClassGroupViewSet(viewsets.ModelViewSet):
    queryset=smodels.ClassGroup.objects.all()
    serializer_class=sbserializers.ClassGroupSerializer
    filterset_fields=['school']

class SectionViewSet(viewsets.ModelViewSet):
    queryset=smodels.Section.objects.all()
    serializer_class=sbserializers.SectionSerializer
    filterset_fields=['school']

class TicketViewSet(viewsets.ModelViewSet):
    queryset=smodels.Ticket.objects.all()
    serializer_class=sbserializers.TicketSerializer
    filterset_fields=['school']

class TicketMessageViewSet(viewsets.ModelViewSet):
    queryset=smodels.TicketMessage.objects.all()
    serializer_class=sbserializers.TicketMessageSerializer
    filterset_fields=['school']

class TeacherAttendanceViewSet(viewsets.ModelViewSet):
    queryset=smodels.TeacherAttendance.objects.all()
    serializer_class=sbserializers.TeacherAttendanceSerializer
    filterset_fields=['school']

class SubjectViewSet(viewsets.ModelViewSet):
    queryset=smodels.Subject.objects.all()
    serializer_class=sbserializers.SubjectSerializer
    filterset_fields=['school']

class StudentRequestViewSet(viewsets.ModelViewSet):
    queryset=smodels.StudentRequest.objects.all()
    serializer_class=sbserializers.StudentRequestSerializer
    filterset_fields=['school']

class SettingsViewSet(viewsets.ModelViewSet):
    queryset=smodels.settings.objects.all()
    serializer_class=sbserializers.SettingsSerializer
    filterset_fields=['school']

class RunningYearViewSet(viewsets.ModelViewSet):
    queryset=smodels.RunningYear.objects.all()
    serializer_class=sbserializers.RunningYearSerializer
    filterset_fields=['school']

class ExamViewSet(viewsets.ModelViewSet):
    queryset=smodels.Exam.objects.all()
    serializer_class=sbserializers.ExamSerializer
    filterset_fields=['school']

class OnlineExamViewSet(viewsets.ModelViewSet):
    queryset=smodels.OnlineExam.objects.all()
    serializer_class=sbserializers.OnlineExamSerializer
    filterset_fields=['school']

class ReportsViewSet(viewsets.ModelViewSet):
    queryset=smodels.Reports.objects.all()
    serializer_class=sbserializers.ReportsSerializer
    filterset_fields=['school']

class ResponseViewSet(viewsets.ModelViewSet):
    queryset=smodels.Response.objects.all()
    serializer_class=sbserializers.ResponseSerializer
    filterset_fields=['school']