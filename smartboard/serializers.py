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

class ClassGroupSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.ClassGroup
        fields='__all__'

class SectionSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Section
        fields='__all__'

class TicketSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Ticket
        fields='__all__'

class TicketMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.TicketMessage
        fields='__all__'

class TeacherAttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.TeacherAttendance
        fields='__all__'

class SubjectSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Subject
        fields='__all__'

class StudentRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.StudentRequest
        fields='__all__'

class SettingsSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.settings
        fields='__all__'

class RunningYearSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.RunningYear
        fields='__all__'

class ExamSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Exam
        fields='__all__'

class OnlineExamSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.OnlineExam
        fields='__all__'

class ReportsSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Reports
        fields='__all__'

class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Response
        fields='__all__'

class RemarksSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Remarks
        fields='__all__'

class QuestionPaperSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.QuestionPaper
        fields='__all__'

class QuestionBankSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.QuestionBank
        fields='__all__'

class PollsSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Polls
        fields='__all__'

class PollResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.PollResponse
        fields='__all__'

class PendingUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.PendingUsers
        fields='__all__'

class OnlineUsersSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.OnlineUsers
        fields='__all__'

class NotificationSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Notification
        fields='__all__'

class OnlineExamResultSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.OnlineExamResult
        fields='__all__'

class NoticeMessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.NoticeMessage
        fields='__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.News
        fields='__all__'

class MessageThreadSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.MessageThread
        fields='__all__'

class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Message
        fields='__all__'

class MarkSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Mark
        fields='__all__'

class LiveSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Live
        fields='__all__'

class LibrarianSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Librarian
        fields='__all__'

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.Language
        fields='__all__'

class HomeWorkSerializer(serializers.ModelSerializer):
    class Meta:
        model=smbmodels.HomeWork
        fields='__all__'