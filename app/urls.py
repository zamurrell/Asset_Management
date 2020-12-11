
from django.urls import path
from . import views

urlpatterns = [
    path('welcome', views.welcome),
    path('types', views.types),
    path('wish', views.wish),
]
