from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def welcome(request):
    return HttpResponse('<h1>Routing successful</h1>')


def types(request):
    current_time = str(datetime.datetime.now())
    return render(request, 'types.html', {'now': current_time})
