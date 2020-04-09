from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test_view1(request):
    return HttpResponse ("<h1>This is view 1</h1>")

def test_view2(request):
    return HttpResponse ("<h1>This is view 2</h1>")

def test_view3(request):
    return HttpResponse ("<h1>This is view 3</h1>")

def test_view4(request):
    return HttpResponse ("<h1>This is view 4</h1>")