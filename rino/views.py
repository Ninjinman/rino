from django.shortcuts import render
from django.http import JsonResponse

def slot_game(request):
    return render(request, 'rino/slot_game.html')

def game(request):
    settingtmt = [293.8,284.9,276.5,260.0,243.6,233.2]
    