from django.db import models
time = (
    ("09","09.00 to 10.30"),
    ("1030","10.30 to 12.00"),
    ("12","12.00 to 01.30"),
    ("02","02.00 to 03.30"),
    ("330","03.30 to 05.00"),
    ("saturday","Saturday"),
    )
status = (
    ("doing","Doing"),
    ("complete","Complete"),
    ("break","Break"),
    ("drop","Drop")
    )
class Course(models.Model):
    course=models.CharField(max_length=100)
    def __str__(self):
        return self.course
class Student(models.Model):
    invoiceno=models.CharField(max_length=5, unique=True)
    name=models.CharField(max_length=50)
    course=models.ForeignKey(Course, on_delete=models.CASCADE)
    batchtime=models.CharField(choices=time, max_length=20)
    bsd=models.DateField(null=True)
    phone1=models.CharField(max_length=12, null=True, blank=True)
    phone2=models.CharField(max_length=12, null=True,blank=True)
    place=models.CharField(max_length=30, null=True, blank=True)
    bed=models.DateField(null=True, blank=True)
    staus=models.CharField(choices=status,max_length=10)
    def __str__(self):
        return self.invoiceno
class Subject(models.Model):
    subject=models.CharField(max_length=100)
    def __str__(self):
        return self.subject
class Data(models.Model):
    invoiceno=models.CharField(max_length=5)
    date=models.DateField()
    subject=models.ForeignKey(Subject,on_delete=models.CASCADE)
    report=models.TextField(max_length=200)
    def __str__(self):
        return self.invoiceno
class Fees(models.Model):
    invoiceno=models.CharField(max_length=5)
    name=models.CharField(max_length=40, null=True)
    batchtime=models.CharField(max_length=20, null=True)
    course=models.CharField(max_length=20, null=True)
    fees=models.IntegerField()
    duedate=models.DateField()
    paiddate=models.DateField(blank=True, null=True)
    paidamount=models.IntegerField(blank=True, null=True)
    def __str__(self):
        return self.invoiceno


