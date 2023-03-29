from django.urls import path
from . import views

# URLConf (URL Configuration/s)
urlpatterns = [
    path('hello', views.say_hello),
    path('date', views.current_datetime)
]