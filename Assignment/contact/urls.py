from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='contact'),
    path('forms/', views.forms, name='forms'),
    path('submited/', views.submit, name='submited')
  
]
