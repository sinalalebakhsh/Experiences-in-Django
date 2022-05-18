from django.shortcuts import render

def homepage(request):
    return render(request, 'home/homepage.html')


def rooot(request):
    return render(request, 'rooot.html')

