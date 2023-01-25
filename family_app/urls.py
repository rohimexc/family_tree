from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
     path('', views.index, name='index'),
     path('login', views.login, name='login'),
     path('register', views.register, name='register'),
     path('cb-admin', views.admin, name='cb-admin'),
     path('database', views.database, name='database'),
     path('tambah-keluarga', views.tambahKeluarga, name='tambah-keluarga'),
     path('akun', views.akun, name='akun'),
]