from django.urls import path
from .views import EmployeeList,EmployeeDetail

urlpatterns=[
    path('<int:pk>/',EmployeeDetail.as_view()),
    path('',EmployeeList.as_view()),
]
