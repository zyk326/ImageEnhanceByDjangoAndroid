"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls.py import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls.py'))
"""
from django.contrib import admin
from django.urls import path, include

from django.conf import settings
from django.conf.urls.static import static

from book import views
from . import view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('movie/', include('movie.urls')),

    path('book/', include('book.urls')),

    path('font/', include('font.urls')),

    path('addcookie/', view.add_cookie, name='add_cookie'),

    path('delcookie/', view.del_cookie, name='del_cookie'),

    path('addses/', view.add_ses, name='add_ses'),

    path('getses/', view.get_ses, name='del_ses'),

    path('', view.login, name='login'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
