from django.urls import path
from data import views as data
from . import views

urlpatterns = [
    path("", views.exam, name="exam"),
    path("addstudent", views.addstudent, name="addstudent"),
    path('getstudent/', data.getstudent, name="getstudent"),
    path('getexamid/', views.getexamid, name="getexamid"),
    path('getexamdata/', views.getexamdata, name="getexamdata"),
    path('examlist/', views.examlist, name="examlist"),
]