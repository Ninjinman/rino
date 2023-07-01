from django.shortcuts import render

def slot_game(request):
    return render(request, 'rino/slot_game.html')
