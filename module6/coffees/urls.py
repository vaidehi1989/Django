
from django.urls import path

from . import views

urlpatterns = [
	path('', views.homePageView, name='listcoffees'),
	path('coffee/<int:pk>/', views.coffeeDetailView, name='detail_view'),


]



