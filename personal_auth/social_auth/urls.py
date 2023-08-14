from django.urls import path , include
from .views import *
urlpatterns = [
    path('' , index,name="sign-log"),
    path('home/', home,name="home"),
    path('logout/', logout,name="logout")
]
