from django.urls import path
from rest_framework.routers import SimpleRouter
import views as pviews

router=SimpleRouter()
router.register('tester',pviews.TesterViewSet,basename='tester')
router.register('products',pviews.ProductViewSet,basename='products')
router.register('rejections',pviews.RejectionViewSet,basename='rejections')
router.register('positions',pviews.PositionViewSet,basename='positions')
router.register('authoritynote',pviews.AuthorityNoteViewSet,basename='authoritynote')
router.register('transactions',pviews.TransactionViewSet,basename='transactions')
router.register('userelement',pviews.UserElementViewSet,basename='userelement')
router.register('company',pviews.CompanyViewSet,basename='company')
router.register('companybranch',pviews.CompanyBranchViewSet,basename='companybranch')
router.register('affordability',pviews.AffordabilityViewSet,basename='affordability')
router.register('user',pviews.UserViewSet,basename='user')
router.register('payment',pviews.PaymentViewSet,basename='payment')
router.register('mandate',pviews.MandateViewSet,basename='mandate')
router.register('employee',pviews.EmployeeViewSet,basename='employee')
router.register('bank',pviews.BankViewSet,basename='bank')
router.register('bankbranch',pviews.BankBranchViewSet,basename='bankbranch')
router.register('element',pviews.ElementViewSet,basename='element')
router.register('elementcategory',pviews.ElementCategoryViewSet,basename='elementcategory')
router.register('elementgroup',pviews.ElementGroupViewSet,basename='elementgroup')
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

