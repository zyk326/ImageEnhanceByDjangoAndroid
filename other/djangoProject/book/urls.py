from django.urls import path
from . import views

urlpatterns=[
    path('', views.index, name='book_index'),

    path('add/', views.add_book, name='add_book'),

    path('query/', views.query_book, name='query_book'),
]
