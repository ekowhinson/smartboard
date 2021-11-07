from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import UserViewSet, AffordabilityViewSet, CompanyBranchViewSet, CompanyViewSet,EmployeeViewSet, MandateViewSet,PaymentViewSet,ActivityLogList,LoginAttemptsList

router=SimpleRouter()
router.register('company',CompanyViewSet,basename='company')
router.register('companybranch',CompanyBranchViewSet,basename='companybranch')
router.register('affordability',AffordabilityViewSet,basename='affordability')
router.register('user',UserViewSet,basename='user')
router.register('payment',PaymentViewSet,basename='payment')
router.register('mandate',MandateViewSet,basename='mandate')
router.register('employee',EmployeeViewSet,basename='employee')

urlpatterns=router.urls


#[
 #   path('activitylogs/',ActivityLogList.as_view()),
  #  path('employees/<int:pk>/',EmployeeDetail.as_view()),
   # path('users/',UserList.as_view()),
    #path('users/<int:pk>/',UserDetails.as_view()),
    #path('employees/',EmployeeList.as_view()),
    #path('loginattemps/',LoginAttemptsList.as_view()),
    #path('companybranches/',CompanyBranchList.as_view()),
    #path('companybranches/<int:pk>',CompanyBranchDetails.as_view()),
    #path('affordability/',AffordabilityList.as_view()),
    #path('affordability/<int:pk>',AffordabilityDetails.as_view()),
    #path('payments/',PaymentList.as_view()),
    #path('payments/<int:pk',PaymentDetails.as_view()),
    #path('mandate/<int:pk',MandateDetails.as_view()),
    #path('mandate/',MandateList.as_view())
#]

