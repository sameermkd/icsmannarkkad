from django.db import models
from data.models import Course

class Exam(models.Model):
    examid=models.CharField(max_length=10)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    module=models.CharField(max_length=10, null=True, blank=True)
    examlink=models.CharField(max_length=100)
    def __str__(self):
        return self.examid
class ExamStudent(models.Model):
    invoiceno=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    phone=models.CharField(max_length=15)
    course=models.CharField(max_length=20)
    examid=models.CharField(max_length=20)
    examlink=models.CharField(max_length=100)
    dateofexam=models.DateField()
    examtime=models.TimeField()
    def __str__(self):
        return self.invoiceno