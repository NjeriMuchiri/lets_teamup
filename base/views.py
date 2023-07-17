from django.shortcuts import render
from .models import Room
#Create your views here.
def home(request):
    rooms = [
        {'id': 1, 'name': 'let us learn Python!'},
        {'id': 2, 'name': 'Design with me'},
        {'id': 3, 'name': 'Frontend developers'},
    ]
    rooms = Room.objects.all()
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def rooms(request, pk):
    rooms = [
        {'id': 1, 'name': 'let us learn Python!'},
        {'id': 2, 'name': 'Design with me'},
        {'id': 3, 'name': 'Frontend developers'},
    ]
    room = Room.objects.get(id=pk)
    context = {'room': room}
    return render(request, 'base/room.html', context)

def createRoom(request):
    context = {}
    return render(request, 'base/room_form.html', context)
