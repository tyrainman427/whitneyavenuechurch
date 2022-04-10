from django.urls import path
from whitneyapp.views import *

app_name = "whitney"

urlpatterns = [
    path('', home, name="home"),
    path('about/', about,name="about"),
    path('pastor/', pastor,name="pastor"),
    path('sermon/', sermon,name="sermon"),
    path('service/', service,name="service"),
    path('cristo/', cristo,name="cristo"),
    path('contact/', contact,name="contact"),
    path('events/', events,name="events"),
    
] 
