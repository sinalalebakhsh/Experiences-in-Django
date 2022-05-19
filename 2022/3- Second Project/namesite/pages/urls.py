from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('hackme.space/', views.hackme_space, name='hackme_space'),
]
