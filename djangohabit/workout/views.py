from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

workouts = [{
    'muscle': 'chest',
    'machine': 'chest-fly',
    'numberofset': '3',
    'numberofrep': '10',
},
 {'muscle': 'shoulder',
    'machine': 'shoulder-press',
    'numberofset': '3',
    'numberofrep': '10',}]

def home(request):
    context = {
        'workouts': workouts
    }
    return render(request, 'workout/home.html', context)

def coding(request):
    return render(request, 'workout/coding.html')