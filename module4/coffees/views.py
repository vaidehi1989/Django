
from .models import Coffee
from django.shortcuts import render

def homePageView(request):
    coffees = Coffee.objects.all()
    # coffees/templates/listcoffees.html
    return render(request, 'listcoffees.html', {'coffees_list' : coffees})
