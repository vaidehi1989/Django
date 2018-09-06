
from .models import Coffee
from django.shortcuts import render, get_object_or_404



def homePageView(request):
    coffees = Coffee.objects.all()
    return render(request, 'listcoffees.html', {'coffees' : coffees})


# View a specific coffee
def coffeeDetailView(request, pk):
    coffee = get_object_or_404(Coffee, pk=pk)
    return render(request, 'coffee_detail.html', {'coffee': coffee})
