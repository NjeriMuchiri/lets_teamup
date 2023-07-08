from django.shortcuts import render

rooms = [
    {'id': 1, 'name': 'let us learn Python!'},
    {'id': 2, 'name': 'Design with me'},
    {'id': 3, 'name': 'Frontend developers'},
]
# Create your views here.
def home(request):
    context = {'rooms': rooms}
    return render(request, 'home.html', context)

def rooms(request):
    return render(request, 'room.html')
