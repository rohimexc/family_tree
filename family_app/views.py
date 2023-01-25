
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *

def index(request):
    return render(request,'family_app/index.html')

def login(request):
    if request.method=='POST':

        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        try:
            user=User.objects.get(username=username)
        except: 
            messages.error(request,'User belum terdaftar')
        user=authenticate(request, username=username, password=password)     
        if user is not None:
            return redirect('cb-admin')
    return render(request,'family_app/login.html')

def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            messages.success(request, "Registration successful." )
            return redirect("akun")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    context={'form':form}
    return render (request, 'family_app/register.html',context)

@login_required(login_url='login')
def admin(request):
    return render(request,'family_app/admin.html')

@login_required(login_url='login')
def database(request):
    return render(request,'family_app/database.html')

def tambahKeluarga(request):
    family=Family.objects.all()
    form = Familyform()
    if request.method=='POST':
        form=Familyform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('database')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'family':family}
    return render(request, 'family_app/tambah_keluarga.html',context)

@login_required(login_url='login')
def akun(request):
    user=User.objects.all()
    context={'user':user}
    return render(request,'family_app/akun.html',context)

