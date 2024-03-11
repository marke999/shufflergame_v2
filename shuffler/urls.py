"""shuffler URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
#from django.conf.urls import url
from django.urls import path
from django.contrib import admin
from shuffler_app.views import homepage, game, login, shuffleword, register, process_form, store_input, debug

urlpatterns = [
    path('homepage/', homepage, name='homepage'),
    path('game/', game, name='game'),
    path('login/', login, name='login'),
    path('shuffleword/', shuffleword, name='shuffleword'),
    path('register/', register, name='register'),
    path('register/process_form', process_form, name='process_form'),
    path('shuffleword/store_input/', store_input, name='store_input'),
    path('debug', debug, name='debug'),
]
