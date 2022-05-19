from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('hackme.space2022/', views.hackme_space, name='hackme.space'),
    path('sinanis/', views.sinanis, name='hackme space'),

]
