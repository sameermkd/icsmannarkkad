from django.shortcuts import render
from data.models import Student
from .utils import render_to_pdf
from dateutil.parser import parse
from dateutil.rrule import rrule, DAILY, MO, TU, WE, TH, FR, SA

def index(request):
    return render(request,"attendence/index.html")
def generate(request):
    date=[]
    exclude=["complete","drop","break"]
    if request.method=='POST':
        start=request.POST['startingdate']
        end=request.POST['endingdate'] 
        batch=request.POST['batch']
        print(batch)
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