# templateExtendingDemo.views.py

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

def aboutPageView(request):
	return render(request, 'aboutus.html')

def homePageView(request):
	return render(request, 'index.html')

