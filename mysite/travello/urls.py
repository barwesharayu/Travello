"""mysite URL Configuration

The is copied from mysite URLs.py. 
made changes by myself
"""
from django.urls import path

from . import views

urlpatterns = [
	path('',views.index, name = 'index'),
]