from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def bio(request):
    return HttpResponse('<h1>This is string response for mia bio</h1>')
def mbio(request):
    return render(request,'mbio.html')