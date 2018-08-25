# templateExtendingDemo.urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('about/', views.aboutPageView, name='about'), 
]
