from django.urls import path  
from .views import *
urlpatterns = [
     path('register/',register),
    path('login/',login),
    path('logout/',logout),
    path('verification/',verify_otp),
]