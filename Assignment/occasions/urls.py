from django.urls import path
from . import views

urlpatterns = [
    path('', views.occasions, name='occasions'),
    path('any/', views.any, name='any'),
    path('thank/', views.thank, name='thank'),
]
