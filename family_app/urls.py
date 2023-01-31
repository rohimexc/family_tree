from django.contrib import admin
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
     path('', views.index, name='index'),
     path('login', views.login_request, name='login'),
     path('register', views.register, name='register'),
     path('cb-admin', views.admin, name='cb-admin'),
     path('database', views.database, name='database'),
     path('tambah-keluarga', views.tambahKeluarga, name='tambah-keluarga'),
     path('hapus-keluarga/<str:id>', views.hapusKeluarga, name='hapus-keluarga'),
     path('akun', views.akun, name='akun'),
]+  static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)