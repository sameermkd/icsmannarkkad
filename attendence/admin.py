from django.contrib import admin
from . models import Attendence

class AttendenceAdmin(admin.ModelAdmin):
    list_display=('name','course','attendence','date')
admin.site.register(Attendence,AttendenceAdmin)