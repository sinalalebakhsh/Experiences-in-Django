from django.urls import path
from . import views


urlpatterns = [
    path('', views.homepage, name='home page'),
    path('rooot/', views.rooot, name='rooot page'),
    path('sinanis/', views.sinanis, name='sinanis page'),

]
