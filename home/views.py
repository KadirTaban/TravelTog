from django.shortcuts import render

from home.models import Journey

# Create your views here.


def home(request):
    journeys = Journey.objects.all()
    print(journeys)

    return render(request, 'home.html', {
        'journeys':journeys
    })