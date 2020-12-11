from django.shortcuts import render
from django.http import HttpResponse
import datetime

# Create your views here.


def welcome(request):
    return HttpResponse('<h1>Routing successful</h1>')


def types(request):
    current_time = str(datetime.datetime.now())
    return render(request, 'types.html', {'now': current_time})


def send_types(request):
    types = ['Computers', 'Monitors', 'Desks', 'Servers', 'Peripherals']
    creator = "Zach Murrell"
    return render(request, 'list_types.html', {'types': types, 'creator': creator})


def wish(request):
    if 'name' in request.GET:
        name = request.GET['name']
    else:
        name = "Guest"
    return HttpResponse(f'<h1>Hello {name}</h1>')
