
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate #add this
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from .models import *
from datetime import date
import json
from django.http import JsonResponse
from django.utils import timezone
today = timezone.now().date()
def index(request):
    family=list(Family.objects.values('id','pids','mid','fid','name', 'gender', 'born', 'country', 'city', 'phone','email'))
    family_members=Family.objects.filter(born__month=today.month)
    nearest_birthday = None
    nearest_birthday_diff = 999
    databirthday=[]
    for member in family_members:
        # Get the difference between the member's birthday and today
        birthday_diff = abs((member.born.replace(year=today.year) - today).days)
        if birthday_diff < nearest_birthday_diff:
            nearest_birthday = member
            nearest_birthday_diff = birthday_diff
        # Output the name of the nearest birthday
        if nearest_birthday:
            person={'name' : nearest_birthday.name, 'sisahari':nearest_birthday_diff, 'born':nearest_birthday.born}
            databirthday.append(person)
        else:
            databirthday=[]
            print("No birthdays in the current month.")
    new_list = [{k: v for k, v in d.items() if v is not None} for d in family]
    new_list = [{k: [v] if k == 'pids' else v for k, v in d.items()} for d in new_list]
    for i in range(len(new_list)):
        for key, value in new_list[i].items():
            if isinstance(value, date):
                new_list[i][key] = value.strftime('%Y-%m-%d')
    context={'data': json.dumps(new_list), 'databirthday': databirthday}
    return render(request,'family_app/index.html',context)

def login_request(request):
    if request.method == "POST":
        username=request.POST.get('username').lower()
        password=request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('cb-admin')
        else:
            messages.error(request,"Invalid username or password.")
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
    family_members=Family.objects.filter(born__month=today.month)
    nearest_birthday = None
    nearest_birthday_diff = 999
    databirthday=[]
    for member in family_members:
        # Get the difference between the member's birthday and today
        birthday_diff = abs((member.born.replace(year=today.year) - today).days)
        if birthday_diff < nearest_birthday_diff:
            nearest_birthday = member
            nearest_birthday_diff = birthday_diff
        # Output the name of the nearest birthday
        if nearest_birthday:
            person={'name' : nearest_birthday.name, 'sisahari':nearest_birthday_diff, 'born':nearest_birthday.born}
            databirthday.append(person)
        else:
            databirthday=[]
            print("No birthdays in the current month.")
    family=list(Family.objects.values('id','pids','mid','fid','name', 'gender', 'born','death', 'country', 'city', 'phone','email'))
    new_list = [{k: v for k, v in d.items() if v is not None} for d in family]
    new_list = [{k: [v] if k == 'pids' else v for k, v in d.items()} for d in new_list]
    for i in range(len(new_list)):
        for key, value in new_list[i].items():
            if isinstance(value, date):
                new_list[i][key] = value.strftime('%Y-%m-%d')
    context={'data': json.dumps(new_list), 'databirthday':databirthday}
    return render(request,'family_app/admin.html',context)

@login_required(login_url='login')
def database(request):
    family=Family.objects.all()
    context={'family':family}
    return render(request,'family_app/database.html',context)

@login_required(login_url='login')
def tambahKeluarga(request):
    citydb=OptionCity.objects.all()
    countrydb=OptionCountry.objects.all()
    form = Familyform()
    for row in OptionCity.objects.all().reverse():
        if OptionCity.objects.filter(city=row.city).count() > 1:
            row.delete()
    for row in OptionCountry.objects.all().reverse():
        if OptionCountry.objects.filter(country=row.country).count() > 1:
            row.delete()
    if request.method=='POST':
        form=Familyform(request.POST,request.FILES)
        if form.is_valid():
            city=request.POST.get('city')
            country=request.POST.get('country')
            cityOption=OptionCity.objects.create(
                city=city
            )
            cityOption.save()

            countryOption=OptionCountry.objects.create(
                country=country
            )
            countryOption.save()

            instance = form.save(commit=False)
            relation= form.cleaned_data['relation']
            relation_from=form.cleaned_data['relation_from']
            relation_idf=relation_from.idf
            if relation == 'suami' or  relation == 'istri':
                
                instance.pids=relation_idf
                instance.city=city
                instance.country=country
                instance.save()
                optionFamily=OptionFamily.objects.create(
                    idf=instance.id,
                    name=form.cleaned_data['name'],
                    pids=relation_idf
                )
                optionFamily.save()
                optionFamilyGet=OptionFamily.objects.get(idf=relation_idf)
                optionFamilyGet.pids=instance.id
                optionFamilyGet.save()
            elif relation == 'anak perempuan' or  relation == 'anak laki-laki':
                instance.fid=relation_idf
                instance.mid=relation_from.pids
                instance.city=city
                instance.country=country
                instance.save()
                optionFamilyGet=OptionFamily.objects.create(
                    idf=instance.id,
                    name=form.cleaned_data['name'],
                    fid=relation_idf,
                    mid=relation_from.pids
                )
                optionFamilyGet.save()
            else:
                instance.city=city
                instance.country=country
                instance.save()
                gender=form.cleaned_data['gender']

                optionFamilyGet=OptionFamily.objects.get(idf=relation_idf)
                if gender == 'male':
                    optionFamilyGet.mid=instance.id
                else:
                    optionFamilyGet.fid=instance.id
                optionFamilyGet.save()

            messages.success(request,'Berhasil Simpan Data')

            return redirect('database')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'city':citydb, 'country':countrydb}
    return render(request, 'family_app/tambah_keluarga.html',context)

@login_required(login_url='login')
def hapusKeluarga(request,id):
    family=Family.objects.get(id=id)
    if request.method == "POST":
        family.delete()
        messages.success(request, 'Data berhasil dihapus')
    return redirect('database')

@login_required(login_url='login')
def akun(request):
    user=User.objects.all()
    context={'user':user}
    return render(request,'family_app/akun.html',context)

