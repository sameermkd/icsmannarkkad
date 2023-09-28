from django.contrib import admin
from .models import Data, Fees, Subject, Student, Course

class DataAdmin(admin.ModelAdmin):
    list_display=('invoiceno','date')
admin.site.register(Data,DataAdmin)
class FeesModel(admin.ModelAdmin):
    list_display=('invoiceno','name','course','batchtime','duedate','fees','paiddate','paidamount')
class StudentModel(admin.ModelAdmin):
    list_display=('invoiceno','name','course','batchtime','phone1','staus')
admin.site.register(Student, StudentModel)
admin.site.register(Fees,FeesModel)
admin.site.register(Subject)
admin.site.register(Course)