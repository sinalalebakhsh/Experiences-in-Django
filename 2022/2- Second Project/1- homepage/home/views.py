from django.shortcuts import render

def homepage(request):
    return render(request, 'home/homepage.html')


def rooot(request):
    context = {
        'page_name' : 'Rooot'
    }
    return render(request, 'rooot.html', context)

def sinanis(request):
    return render(request, 'home/sinanis.html')



