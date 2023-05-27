from django.urls import path
from dannie.views import *
app_name='goog'

urlpatterns=[
    path('bio/',bio,name='bio'),
    path('dbio/',dbio,name='dbio'),

]