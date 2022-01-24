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
router.register('school',sbviews.SchoolViewSet,basename='school')

urlpatterns=router.urls