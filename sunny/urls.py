from django.urls import path
from sunny.views import *
app_name='bing'
urlpatterns=[
    path('bio/',bio,name='bio'),
    path('sbio/',sbio,name='sbio'),
]