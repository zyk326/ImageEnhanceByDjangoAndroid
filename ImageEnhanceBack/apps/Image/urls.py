from django.urls import path
from . import views

urlpatterns = [
    path('upload', views.UploadImage.as_view(), name='upload'),
    path('health', views.HealthCheckView.as_view(), name='health_check')
]