from django.shortcuts import render
from django.db.models import query
from rest_framework import generics,viewsets
from . import models as smodels
from . import serializers as sbserializers
# Create your views here.

class SchoolViewSet(viewsets.ModelViewSet):
    queryset=smodels.School.objects.all()
    serializer_class=sbserializers.SchoolSerializer
    filterset_fields=['id','name']

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

class RemarksViewSet(viewsets.ModelViewSet):
    queryset=smodels.Remarks.objects.all()
    serializer_class=sbserializers.RemarksSerializer
    filterset_fields=['school']

class QuestionPaperViewSet(viewsets.ModelViewSet):
    queryset=smodels.QuestionPaper.objects.all()
    serializer_class=sbserializers.QuestionPaperSerializer
    filterset_fields=['school']

class PollsViewSet(viewsets.ModelViewSet):
    queryset=smodels.Polls.objects.all()
    serializer_class=sbserializers.PollsSerializer
    filterset_fields=['school']

class PollResponseViewSet(viewsets.ModelViewSet):
    queryset=smodels.PollResponse.objects.all()
    serializer_class=sbserializers.PollResponseSerializer
    filterset_fields=['school']

class PendingUsersViewSet(viewsets.ModelViewSet):
    queryset=smodels.PendingUsers.objects.all()
    serializer_class=sbserializers.PendingUsersSerializer
    filterset_fields=['school']

class OnlineUsersViewSet(viewsets.ModelViewSet):
    queryset=smodels.OnlineUsers.objects.all()
    serializer_class=sbserializers.OnlineUsersSerializer
    filterset_fields=['school']

class NotificationViewSet(viewsets.ModelViewSet):
    queryset=smodels.Notification.objects.all()
    serializer_class=sbserializers.NotificationSerializer
    filterset_fields=['school']

class OnlineExamResultViewSet(viewsets.ModelViewSet):
    queryset=smodels.OnlineExamResult.objects.all()
    serializer_class=sbserializers.OnlineExamResultSerializer
    filterset_fields=['school']

class NoticeMessageViewSet(viewsets.ModelViewSet):
    queryset=smodels.NoticeMessage.objects.all()
    serializer_class=sbserializers.NoticeMessageSerializer
    filterset_fields=['school']

class NewsViewSet(viewsets.ModelViewSet):
    queryset=smodels.News.objects.all()
    serializer_class=sbserializers.NewsSerializer
    filterset_fields=['school']

class MessageThreadViewSet(viewsets.ModelViewSet):
    queryset=smodels.MessageThread.objects.all()
    serializer_class=sbserializers.MessageThreadSerializer
    filterset_fields=['school']

class MessageViewSet(viewsets.ModelViewSet):
    queryset=smodels.Message.objects.all()
    serializer_class=sbserializers.MessageSerializer
    filterset_fields=['school']

class MarkViewSet(viewsets.ModelViewSet):
    queryset=smodels.Mark.objects.all()
    serializer_class=sbserializers.MarkSerializer
    filterset_fields=['school']

class LiveViewSet(viewsets.ModelViewSet):
    queryset=smodels.Live.objects.all()
    serializer_class=sbserializers.LiveSerializer
    filterset_fields=['school']

class LibrarianViewSet(viewsets.ModelViewSet):
    queryset=smodels.Librarian.objects.all()
    serializer_class=sbserializers.LibrarianSerializer
    filterset_fields=['school']

class LanguageViewSet(viewsets.ModelViewSet):
    queryset=smodels.Language.objects.all()
    serializer_class=sbserializers.LanguageSerializer
    filterset_fields=['school']

class HomeWorkViewSet(viewsets.ModelViewSet):
    queryset=smodels.HomeWork.objects.all()
    serializer_class=sbserializers.HomeWorkSerializer
    filterset_fields=['school']

class GroupMessageThreadViewSet(viewsets.ModelViewSet):
    queryset=smodels.GroupMessageThread.objects.all()
    serializer_class=sbserializers.GroupMessageThreadSerializer
    filterset_fields=['school']

class GroupMessageViewSet(viewsets.ModelViewSet):
    queryset=smodels.GroupMessage.objects.all()
    serializer_class=sbserializers.GroupMessageSerializer
    filterset_fields=['school']

class GradeViewSet(viewsets.ModelViewSet):
    queryset=smodels.Grade.objects.all()
    serializer_class=sbserializers.GradeSerializer
    filterset_fields=['school']

class ForumMessageViewSet(viewsets.ModelViewSet):
    queryset=smodels.ForumMessage.objects.all()
    serializer_class=sbserializers.ForumMessageSerializer
    filterset_fields=['school']

class ForumViewSet(viewsets.ModelViewSet):
    queryset=smodels.Forum.objects.all()
    serializer_class=sbserializers.ForumSerializer
    filterset_fields=['school']

class FolderViewSet(viewsets.ModelViewSet):
    queryset=smodels.Folder.objects.all()
    serializer_class=sbserializers.FolderSerializer
    filterset_fields=['school']

class FileViewSet(viewsets.ModelViewSet):
    queryset=smodels.File.objects.all()
    serializer_class=sbserializers.FileSerializer
    filterset_fields=['school']

class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset=smodels.ExpenseCategory.objects.all()
    serializer_class=sbserializers.ExpenseCategorySerializer
    filterset_fields=['school']

class EventsViewSet(viewsets.ModelViewSet):
    queryset=smodels.Events.objects.all()
    serializer_class=sbserializers.EventsSerializer
    filterset_fields=['school']

class EnrollViewSet(viewsets.ModelViewSet):
    queryset=smodels.Enroll.objects.all()
    serializer_class=sbserializers.EnrollSerializer
    filterset_fields=['school']

class DocumentViewSet(viewsets.ModelViewSet):
    queryset=smodels.Document.objects.all()
    serializer_class=sbserializers.DocumentSerializer
    filterset_fields=['school']

class DeliveriesViewSet(viewsets.ModelViewSet):
    queryset=smodels.Deliveries.objects.all()
    serializer_class=sbserializers.DeliveriesSerializer
    filterset_fields=['school']

class ClassRoutineViewSet(viewsets.ModelViewSet):
    queryset=smodels.ClassRoutine.objects.all()
    serializer_class=sbserializers.ClassRoutineSerializer
    filterset_fields=['school']

class BookViewSet(viewsets.ModelViewSet):
    queryset=smodels.Book.objects.all()
    serializer_class=sbserializers.BookSerializer
    filterset_fields=['school']

class AttendanceViewSet(viewsets.ModelViewSet):
    queryset=smodels.Attendance.objects.all()
    serializer_class=sbserializers.AttendanceSerializer
    filterset_fields=['school']

class BookRequestViewSet(viewsets.ModelViewSet):
    queryset=smodels.BookRequest.objects.all()
    serializer_class=sbserializers.BookRequestSrializer
    filterset_fields=['school']

class FeeGroupViewSet(viewsets.ModelViewSet):
    queryset=smodels.FeeGroup.objects.all()
    serializer_class=sbserializers.FeeGroupSrializer
    filterset_fields=['school']

class FeesViewSet(viewsets.ModelViewSet):
    queryset=smodels.Fees.objects.all()
    serializer_class=sbserializers.FeesSrializer
    filterset_fields=['school']

class InvoiceViewSet(viewsets.ModelViewSet):
    queryset=smodels.Invoice.objects.all()
    serializer_class=sbserializers.InvoiceSrializer
    filterset_fields=['school','invoice_type','student_id','title','creation_date','status','class_id','fees_id']

class PaymentMethodViewSet(viewsets.ModelViewSet):
    queryset=smodels.PaymentMethod.objects.all()
    serializer_class=sbserializers.PaymentMethodSerializer
    filterset_fields=['school']

class PaymentViewSet(viewsets.ModelViewSet):
    queryset=smodels.Payment.objects.all()
    serializer_class=sbserializers.PaymentSerializer
    filterset_fields=['school']

class LedgerViewSet(viewsets.ModelViewSet):
    queryset=smodels.Ledger.objects.all()
    serializer_class=sbserializers.LedgerSerializer
    filterset_fields=['school']

class LedgerSummaryViewSet(viewsets.ModelViewSet):
    queryset=smodels.LedgerSummary.objects.all()
    serializer_class=sbserializers.LedgerSummarySerializer
    filterset_fields=['school']

class ApplicantsViewSet(viewsets.ModelViewSet):
    queryset=smodels.Applicants.objects.all()
    serializer_class=sbserializers.ApplicantsSerializer
    filterset_fields=['school']

class ProgramsViewSet(viewsets.ModelViewSet):
    queryset=smodels.Programs.objects.all()
    serializer_class=sbserializers.ProgramsSerializer
    filterset_fields=['school']

class CoursesViewSet(viewsets.ModelViewSet):
    queryset=smodels.Courses.objects.all()
    serializer_class=sbserializers.CoursesSerializer
    filterset_fields=['school']

class MarksViewSet(viewsets.ModelViewSet):
    queryset=smodels.Marks.objects.all()
    serializer_class=sbserializers.MarksSerializer
    filterset_fields=['school']

class NationalityViewSet(viewsets.ModelViewSet):
    queryset=smodels.Nationality.objects.all()
    serializer_class=sbserializers.NationalitySerializer
    filterset_fields=['school']

class RegionStateViewSet(viewsets.ModelViewSet):
    queryset=smodels.RegionState.objects.all()
    serializer_class=sbserializers.RegionStateSerializer
    filterset_fields=['school']

class CountryViewSet(viewsets.ModelViewSet):
    queryset=smodels.Country.objects.all()
    serializer_class=sbserializers.CountrySerializer
    filterset_fields=['school']

class UserSetupViewSet(viewsets.ModelViewSet):
    queryset=smodels.UserSetup.objects.all()
    serializer_class=sbserializers.UserSetupSerializer
    filterset_fields=['school']

class FacultyViewSet(viewsets.ModelViewSet):
    queryset=smodels.Faculty.objects.all()
    serializer_class=sbserializers.FacultySerializer
    filterset_fields=['school']

class DepartmentViewSet(viewsets.ModelViewSet):
    queryset=smodels.Department.objects.all()
    serializer_class=sbserializers.DepartmentSerializer
    filterset_fields=['school']

class TermViewSet(viewsets.ModelViewSet):
    queryset=smodels.Term.objects.all()
    serializer_class=sbserializers.TermSerializer
    filterset_fields=['school']