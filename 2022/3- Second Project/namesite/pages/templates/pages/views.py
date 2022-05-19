from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'home.html')


def hackme_space(request):
    return render(request, 'pages/hackme_space.html')

