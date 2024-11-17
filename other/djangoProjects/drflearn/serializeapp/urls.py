from django.urls import path
from .views import merchant, category

app_name = 'serialze'

urlpatterns = [
    path('merchant/', merchant, name='merchant'),
    path('category/', category, name='category'),
]