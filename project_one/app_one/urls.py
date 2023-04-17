from django.urls import path
from app_one.views import *
app_name='nothing'
urlpatterns=[ 
    path('virat',virat,name='virat')
]