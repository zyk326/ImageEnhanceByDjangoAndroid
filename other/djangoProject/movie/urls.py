from django.urls import path
from . import views

# app_name = 'movie'

urlpatterns = [
    path('list', views.movie_list, name="movie_list"),

    path('detail/<str:movie_id>', views.movie_detail, name="movie_detail"),

    path('', views.index, name="index")
]