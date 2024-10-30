from font import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('mod/', views.mod, name = 'model'),
]