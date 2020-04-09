from django.shortcuts import render
import datetime
# Create your views here.
def date_time_view(request):
    date = datetime.datetime.now()
    h = int(date.strftime('%H'))
    msg = 'Hello sir !! Very Very Good'
    if h<12:
        msg = msg +'Morning'
    elif h<16:
        msg = msg +'Afternoon'
    elif h<21:
        msg = msg +'Evening'
    else:
        msg = msg+'Night'

    dt = {'date':date,'msg':msg}    

    return render(request,'testapp/results.html',dt)                