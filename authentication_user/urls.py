from django.urls import path,include
from .views import *

urlpatterns = [
    path('',loginpage,),
    path('logout/',logout_user),
    path('signup/',signup),
    path('logout/',home,name="logout")
   
]
