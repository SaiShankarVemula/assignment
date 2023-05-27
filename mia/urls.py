from django.urls import path
from mia.views import *

app_name='yahoo'

urlpatterns=[
    path('bio/',bio,name='bio'),
    path('mbio/',mbio,name='mbio'),
]