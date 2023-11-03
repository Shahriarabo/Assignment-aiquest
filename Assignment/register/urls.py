from django.urls import path
from . import views

urlpatterns = [
    path('',views.register, name='register'),
    path('login/',views.loginform, name='loginform'),
    path('submited/', views.submit, name='submited'),
    path('logout/', views.logoutforms, name='logout'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('change/', views.change, name='change'),
    path('withoutoldpassword/', views.withoutold, name='withoutoldpassword'),
    
    
  
]
