from django.shortcuts import render
from django.http import HttpResponse
from menu.models import User
# Create your views here.

def home(request):
   return render(request, 'menu/home.html')

def about(request):
    return HttpResponse("This is the about page.")