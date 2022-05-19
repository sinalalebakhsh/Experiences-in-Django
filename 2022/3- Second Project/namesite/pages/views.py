from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    context = {
        'page_name': 'home',
    }
    return render(request, 'home.html', context)


def hackme_space(request):
    context = {
        'page_name': 'Hackme.Space'
    }
    return render(request, 'pages/hackme_space.html', context)


def sinanis(request):
    context = {
        'page_name': 'SinaniS'
    }
    return render(request, 'pages/sinanis.html', context)


