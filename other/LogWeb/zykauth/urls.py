from django.urls import path
from . import views

app_name = 'zykauth'

urlpatterns = [
    path('login', views.zyklogin, name='login'),

    path('logout', views.zyklogout, name='logout'),

    path('register', views.register, name='register'),

    path('captcha', views.send_email_captcha, name='captcha'),
]