from django.shortcuts import render
from data.models import Student
from .utils import render_to_pdf
from dateutil.parser import parse
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR, SA
from . models import Attendence

def index(request):
    if request.method=='POST':
        a=request.POST.getlist("invoiceno"),
        for invoiceno, name, course, attendence, phone1, phone2 in zip(
        request.POST.getlist("invoiceno"),
        request.POST.getlist("name"),
        request.POST.getlist("course"),
        request.POST.getlist("attendence"),
        request.POST.getlist("mob1"),
        request.POST.getlist("mob2"),
        ):
            ex = Attendence.objects.create(
            invoiceno=invoiceno,
            name=name,
            course=course,
            attendence=attendence,
            mob1=phone1,
            mob2=phone2,
            )
            ex.save()
        return render(request, "attendence/index.html")
    return render(request, "attendence/index.html")
def generate(request):
    date=[]
    exclude=["complete","drop","break"]
    if request.method=='POST':
        start=request.POST['startingdate']
        end=request.POST['endingdate'] 
        batch=request.POST['batch']
        if batch=='saturday':
            student=Student.objects.filter(batchtime=batch).exclude(staus__in=exclude)
            date_list = rrule(
                DAILY,
                byweekday=(SA),
                dtstart=parse(start),
            until=parse(end)
            )
            for a in date_list:
                date.append(a.strftime("%d-%a"))
            template_name = "attendence/pdf.html"
            return render_to_pdf(
                template_name,
            {
                "date": date,
                "start":start,
                "end":end,
                "student":student,
                "batch":batch
            },
            )
        else:
            student=Student.objects.filter(batchtime=batch).exclude(staus__in=exclude)
            date_list = rrule(
                DAILY,
                byweekday=(MO,TU,WE,TH,FR),
                dtstart=parse(start),
            until=parse(end)
            )
            for a in date_list:
                date.append(a.strftime("%d-%a"))
            template_name = "attendence/pdf.html"
            return render_to_pdf(
                template_name,
            {
                "date": date,
                "start":start,
                "end":end,
                "student":student,
                "batch":batch
            },
            )
    return render(request,"attendence/generate.html")
def getdata(request):
    exclude=["complete","drop","break"]
    batch=request.GET['batch']
    student=Student.objects.filter(batchtime=batch).exclude(staus__in=exclude)
    context={
        "student":student
        }
    return render(request,"attendence/getdata.html",context)
def leave(request):
    exclude=["complete","drop","break"]
    if request.method=='POST':
        date=request.POST['date']
        student=Attendence.objects.filter(date=date).filter(attendence="leave")
        context={
            "student":student
            }
        return render(request,"attendence/leave.html",context)
    return render(request,"attendence/leave.html")