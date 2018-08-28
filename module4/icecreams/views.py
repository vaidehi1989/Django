from django.views.generic import ListView
from .models import Icecream


class HomePageView(ListView):
    model = Icecream
    template_name = 'listicreams.html' # icecreams/templates/listicreams.html
