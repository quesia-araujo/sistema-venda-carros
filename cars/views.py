from django.shortcuts import render
from cars.models import Car

def cars_view(request):
    cars = Car.objects.all() # buscando dados do banco de dados

    return render(
        request,
        'cars.html',
        {'cars': cars}
    )
