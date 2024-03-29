from django.shortcuts import render
from .models import Race, Driver, DriverPosition, Team


def races(request):

    races = Race.objects.all().order_by('-date')
    drivers = Driver.objects.all().order_by('-points')
    driverPosition = DriverPosition.objects.all().order_by('position')
    team = Team.objects.all()

    context = {
        'races': races,
        'drivers': drivers,
        'driverPosition': driverPosition,
        'title': 'Wyniki wyścigów',

    }
    return render(request, 'races/timetable.html', context)


def tabela_kierowcy(request):
    drivers = Driver.objects.all().order_by('-points')
    context = {
        'drivers': drivers,
        'title': 'Klasyfikacja kierowców',
    }
    return render(request, 'races/tabela_kierowcy.html', context)


def tabela_druzyny(request):
    drivers = Driver.objects.all().order_by('-points')
    teams = {}
    for driver in drivers:
        teams[driver.team] = teams.get(driver.points, 0) + driver.points

    context = {
        'title': 'Klasyfikacja druzyn',
        'teams': teams

    }
    return render(request, 'races/tabela_druzyny.html', context)
