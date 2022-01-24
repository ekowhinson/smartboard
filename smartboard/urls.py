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

urlpatterns=router.urls