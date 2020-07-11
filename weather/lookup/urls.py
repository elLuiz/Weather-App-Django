# include urls from others apps
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('about.html', views.about, name="about")        
]
