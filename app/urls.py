
from django.urls import path
from . import views, interest_views

urlpatterns = [
    path('welcome', views.welcome),
    path('types', views.types),
    path('list_types', views.send_types),
    path('wish', views.wish),
    path('interest', interest_views.interest),
]
