from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def your_view(request):
    return HttpResponse("<h1> Hi this is my current workplace!</h1>")