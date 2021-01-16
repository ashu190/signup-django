from django.contrib import admin
from django.urls import path
from signupApp import views

urlpatterns = [
    path('', views.index, name= "index"),
    path('signup/', views.signup, name= "signup"),
    path('login/', views.login, name= "login"),
    path('logout', views.logout, name= "logout"),
    path('profile/', views.profile, name= "profile"),
    
   
]
