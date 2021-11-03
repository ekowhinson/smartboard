from django.urls import path
from .views import EmployeeList,EmployeeDetail, UserList,ActivityLogList,LoginAttemptsList

urlpatterns=[
    path('activitylogs/',ActivityLogList.as_view()),
    path('<int:pk>/',EmployeeDetail.as_view()),
    path('users/',UserList.as_view()),
    path('employees/',EmployeeList.as_view()),
    path('loginattemps/',LoginAttemptsList.as_view()),
]
