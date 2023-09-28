from django.shortcuts import render
from . models import Systems
def index(request):
    return render(request,"systems/index.html")
def getdata(request):
    batch=request.GET['batch']
    data=Systems.objects.filter(batch=batch)
    context = {
        "data":data
        }
    return render(request,"systems/getdata.html", context)
