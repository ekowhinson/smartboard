from django.urls import path
from .views import EmployeeList,EmployeeDetail,UserList

urlpatterns=[
    path('<int:pk>/',EmployeeDetail.as_view()),
    path('users/',UserList.as_view()),
    path('employees/',EmployeeList.as_view()),
]
