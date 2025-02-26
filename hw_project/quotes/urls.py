from django.urls import path
from . import views

app_name = 'quotes'

urlpatterns = [
    path('', views.main, name='main'),
    path('<int:page>', views.main, name='main_paginate'),
    path('authors/', views.author_list, name='author_list'),
    path('add/author', views.add_author, name='add_author'),
    path('add/quote', views.add_quote, name='add_quote'),
]
