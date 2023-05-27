from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def bio(request):
    return HttpResponse('<h1> This is related to the sunny bio in the string format')
def sbio(request):
    return render(request,'sbio.html')