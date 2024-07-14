from django.views.generic import ListView

from . models import Person
# Create your views here.

class HomeView(ListView):
    
    model = Person
    
    template_name = 'home.html'
