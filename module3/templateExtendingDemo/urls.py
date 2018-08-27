# templateExtendingDemo.urls.py

from django.urls import path
from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path('', views.homePageView, name='home'), # /template/
    path('about/', views.aboutPageView, name='about'), # /template/about/
    path('contact/', TemplateView.as_view(template_name='contactus.html')), # /template/contact/
]
