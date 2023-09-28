from django.urls import path
from . import views

urlpatterns=[
    path("",views.index, name="systems/index"),
    path("getdata/",views.getdata, name="systems/getdata"),
]