
from django.urls import path

from . import views

urlpatterns = [
	# "/coffees/"
	path('', views.homePageView, name='listcoffees'),


]



