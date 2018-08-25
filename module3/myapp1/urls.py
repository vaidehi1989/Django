# myapp1.urls.py

from django.urls import path

from . import views

urlpatterns = [
    path('', views.homePageView, name='home'),
    path('about/', views.aboutPageView, name='about'), # Function based view - url mapping
    path('contact/', views.ContactPageView.as_view(), name='contact'), # Class based view - url mapping
]
