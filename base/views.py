from django.shortcuts import render

#Create your views here.
def home(request):
    rooms = [
        {'id': 1, 'name': 'let us learn Python!'},
        {'id': 2, 'name': 'Design with me'},
        {'id': 3, 'name': 'Frontend developers'},
    ]
    context = {'rooms': rooms}
    return render(request, 'base/home.html', context)

def rooms(request):
    return render(request, 'room.html')
