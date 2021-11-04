from django.urls import path
from .views import AffordabilityDetails, AffordabilityList, CompanyBranchDetails, CompanyBranchList, CompanyDetails,CompanyList, EmployeeList,EmployeeDetail, MandateDetails, MandateList, PaymentDetails, PaymentList, UserList,ActivityLogList,LoginAttemptsList

urlpatterns=[
    path('activitylogs/',ActivityLogList.as_view()),
    path('employees/<int:pk>/',EmployeeDetail.as_view()),
    path('users/',UserList.as_view()),
    path('employees/',EmployeeList.as_view()),
    path('loginattemps/',LoginAttemptsList.as_view()),
    path('companies/',CompanyList.as_view()),
    path('companies/<int:pk>/',CompanyDetails.as_view()),
    path('companybranches/',CompanyBranchList.as_view()),
    path('companybranches/<int:pk>',CompanyBranchDetails.as_view()),
    path('affordability/',AffordabilityList.as_view()),
    path('affordability/<int:pk>',AffordabilityDetails.as_view()),
    path('payments/',PaymentList.as_view()),
    path('payments/<int:pk',PaymentDetails.as_view()),
    path('mandate/<int:pk',MandateDetails.as_view()),
    path('mandate/',MandateList.as_view())
]
