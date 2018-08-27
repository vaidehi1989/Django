
from .models import Coffee
from django.shortcuts import render



def homePageView(request):
    coffees = Coffee.objects.all()
    return render(request, 'listcoffees.html', {'coffees' : coffees})
