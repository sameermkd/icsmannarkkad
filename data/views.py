from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib import messages
from .forms import DataForm
from .models import Fees, Student, Data, Course

def index(request):
    if request.method=='POST':
        form=DataForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Data saved submitted successfully.')
    form=DataForm()
    context = {
        "form":form
        }
    return render(request,"index.html",context)
def fees(request):
    if request.method=='POST':
        feesdate=request.POST['date']
        fees=Fees.objects.filter(duedate=feesdate)
        context = {
        "fees":fees
        }
        return render(request,"fees.html", context)
    return render(request,"fees.html")
def start(request):
    course=Course.objects.all()
    context={
        "course":course
    }
    return render(request, "start.html",context)
def getstart(request):
    invoiceno=request.GET['invoiceno']
    print(len(invoiceno))
    if len(invoiceno)>=5:
        try:
            student=Student.objects.get(invoiceno=invoiceno.upper())
            data=Data.objects.filter(invoiceno=invoiceno.upper())
            context = {
                'student':student,
                'data':data
                }
            return render(request, "getstart.html",context)
        except:
            return  HttpResponseNotFound("Invoice not Found, Please check the invoice number and try again")
        
    return HttpResponse("Enter full Invoice number (Exampe :A0000)")
def getbatch(request):
    exclude=["complete","drop","break"]
    if 'data1' in request.GET:
        batchtime=request.GET['data1']
        student1=Student.objects.filter(batchtime=batchtime).exclude(staus__in=exclude)
        context = {
            "student1":student1,
        }
    if 'data2' in request.GET:
        course=request.GET['data2']
        id=Course.objects.get(course=course)
        student2=Student.objects.filter(course=id).exclude(staus="complete")
        context = {
            "student2":student2,
        }
    return render(request,"getbatch.html", context)
def addfees(request):
    if request.method=='POST':
        invoiceno=request.POST['invoiceno']
        name=request.POST['name']
        batchtime=request.POST['batchtime']
        course=request.POST['course']
        fees=request.POST['fees']
        duedate=request.POST['duedate']
        ex=Fees.objects.create(invoiceno=invoiceno,name=name,batchtime=batchtime,course=course,fees=fees, duedate=duedate)
    return render(request, "addfees.html")
def getstudent(request):
    if request.method=='GET':
        invoiceno=request.GET['invoiceno']
        data=Student.objects.filter(invoiceno=invoiceno)
        context = {
            "data":data,
        }
    return render(request,"getstudent.html",context)
