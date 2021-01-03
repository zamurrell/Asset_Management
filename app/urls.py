
from django.urls import path
from . import views, interest_views, author_views

urlpatterns = [
    path('welcome/', views.welcome),
    path('types/', views.types),
    path('list_types/', views.send_types),
    path('wish/', views.wish),
    path('interest/', interest_views.interest),
    path('interest_post/', interest_views.interest_post),
    # Author URLS
    path('authors/', author_views.list_authors),
    path('add_author/', author_views.add_author),
    path('add_author_form/', author_views.add_author_form),
]
