from django.shortcuts import render
from django.http import HttpResponse
import datetime
# Create your views here.
def time_view(request):
    date = datetime.datetime.now()
    s = "<h1> the current time is "+str(date)+"</h1>"
    return HttpResponse(s)