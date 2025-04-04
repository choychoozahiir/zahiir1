from django.shortcuts import render
from django.http import HttpResponse
from menu.models import Student
# Create your views here.

def home(request):
   students = Student.objects.all()
   return render(request, 'menu/home.html', {'students': students})

def about(request):
    return HttpResponse("This is the about page.")