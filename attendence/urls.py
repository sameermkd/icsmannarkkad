from django.urls import path
from . import views

urlpatterns=[
    path("",views.index, name="attendence/index"),
    path("generate",views.generate, name="attendence/generate"),
    path("getdata/",views.getdata, name="attendence/getdata"),
    path("leave/",views.leave, name="attendence/leave"),
]