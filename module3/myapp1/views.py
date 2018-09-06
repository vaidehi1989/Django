# myapp1.views.py

from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import TemplateView

# Function based Views ------------------------

# Return Response
def homePageView(request):
	return HttpResponse("Hello World!! This is Django app.")

# forwards the request to HTML template
def aboutPageView(request):
	return render(request, 'about.html')

# Class based Views ------------------------

class ContactPageView(TemplateView):
	template_name = 'contact.html'