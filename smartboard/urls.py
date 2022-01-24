from distutils.log import set_verbosity
from posixpath import basename
from django.urls import path
from rest_framework.routers import SimpleRouter
from . import views as sbviews

router=SimpleRouter()
router.register('school',sbviews.SchoolViewSet,basename='school')
router.register('academicsettings',sbviews.AcademicSettingsViewSet,basename='academicsettings')
router.register('academicyear',sbviews.AcademicYearViewSet,basename='academicyear')
router.register('accountrole',sbviews.AccountRoleViewSet,basename='accountrole')
router.register('admin',sbviews.AdminViewSet,basename='admin')
router.register('billingcategory',sbviews.BillingCategoryViewSet,basename='billingcategory')
router.register('dormitory',sbviews.DormitoryViewSet,basename='dormitory')
router.register('teacher',sbviews.TeacherViewSet,basename='teacher')
router.register('parent',sbviews.ParentViewSet,basename='parent')
router.register('level',sbviews.LevelViewSet,basename='level')
router.register('class',sbviews.ClassesViewSet,basename='class')
router.register('student',sbviews.StudentViewSet,basename='student')
router.register('classgroup',sbviews.ClassGroupViewSet,basename='classgroup')
router.register('section',sbviews.SectionViewSet,basename='section')
router.register('ticket',sbviews.TicketViewSet,basename='ticket')
router.register('ticketmessage',sbviews.TicketViewSet,basename='ticketmessage')
router.register('teacherattendance',sbviews.TeacherAttendanceViewSet,basename='teacherattendance')
router.register('studentrequest',sbviews.StudentRequestViewSet,basename='studentrequest')
router.register('settings',sbviews.SettingsViewSet,basename='settings')
router.register('runningyear',sbviews.RunningYearViewSet,basename='runningyear')
router.register('exams',sbviews.ExamViewSet,basename='exams')
router.register('onlineexams',sbviews.OnlineExamViewSet,basename='onlineexams')
urlpatterns=router.urls