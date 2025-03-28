from django.shortcuts import render
from .models import Automobil

def autos(request):
    automoviles = Automobil.objects.all()
    return render(request, 'autos.html', {'automoviles': automoviles})
