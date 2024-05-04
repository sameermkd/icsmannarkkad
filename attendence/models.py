from django.db import models


class Attendence(models.Model):
    invoiceno=models.CharField(max_length=10)
    name=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    attendence=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    mob1=models.CharField(max_length=12,blank=True)
    mob2=models.CharField(max_length=12,blank=True)
    def __str__(self):
        return self.invoiceno
