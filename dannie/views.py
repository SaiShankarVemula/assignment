from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def bio(request):
    return HttpResponse('<h1> This is related to the actress kali@R')
def dbio(request):
    return render(request,'dbio.html')