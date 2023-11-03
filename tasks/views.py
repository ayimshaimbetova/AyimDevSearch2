from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.


def register(request):
    return render(request, 'register.html')

def my_login(request):
    return render(request, 'my-login.html')

def home(request):
    
    clientList = [
        {
            'id': '1',
            'name': 'Ayim Shaim',
            'profession': 'lazybones',

        },
        {
            'id': '2',
            'name': 'Kira',
            'profession': 'call-centerer',

        }

    ]
    context = {'client': clientList}

    return render(request, 'index.html', context = context)