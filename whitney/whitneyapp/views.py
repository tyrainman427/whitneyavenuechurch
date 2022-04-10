from http import cookies
from multiprocessing import context
from django.shortcuts import render
from .models import Event, Sermon

# Create your views here.

def home(request):
    # context = {}
    return render(request, "whitneyapp/index.html")

def about(request):
    return render(request, "whitneyapp/about.html")

def contact(request):
    return render(request, "whitneyapp/contact.html")

def sermon(request):
    sermon = Sermon.objects.all()
    context = { 'sermon': sermon }   
        
    return render(request, "whitneyapp/sermon.html", context)

def service(request):
    return render(request, "whitneyapp/service.html")

def cristo(request):
    return render(request, "whitneyapp/cristo.html")

def events(request):
    event = Event.objects.all()
    print(event)
    context = {
        "event": event
    }
    return render(request, "whitneyapp/events.html", context)

def pastor(request):
    return render(request, "whitneyapp/pastor.html")