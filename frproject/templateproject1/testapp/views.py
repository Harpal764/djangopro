from django.shortcuts import render
import datetime
# Create your views here.
def test_view(request):
    dt = datetime.datetime.now()
    rollno = 101
    Name = 'Harpal singh'
    Marks = 900
    data = {'date':dt,'roll':rollno,'name':Name,'marks':Marks}
    return render(request,'testapp/results.html',data)