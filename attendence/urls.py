from django.urls import path
from . import views

urlpatterns=[
    path("",views.index, name="attendence/index"),
    path("generate",views.generate, name="attendence/index")
]