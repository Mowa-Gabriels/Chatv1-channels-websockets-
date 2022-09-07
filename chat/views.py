
from django.shortcuts import render

# Create your views here.

def lobby(request):

    context={

    }
    return render(request, 'chat/lobby.html', context)