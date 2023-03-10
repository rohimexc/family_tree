
from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate #add this
from django.contrib.auth.decorators import user_passes_test
from django.contrib import messages
from django.contrib.auth.models import User
from .forms import *
from .models import *
from datetime import date
import json
from django.http import JsonResponse
from django.utils import timezone
from django.db.models import Q
import ast

today = timezone.now().date()
def index(request):
    family_members=Family.objects.filter(born__month=today.month)
    anak=0
    cucu=0
    cicit=0
    piut=0
    datacucu=[]
    datacicit=[]
    datapiut=[]
    idanak=[]
    idcucu=[]
    idcicit=[]
    dataanak=Family.objects.filter(Q(mid=17) | Q(fid=17))
    for a in dataanak:
        idanak.append(a.id)
    for a in idanak:
        dc=Family.objects.filter(Q(mid=a) | Q(fid=a))
        for b in dc:
            if b != []:
                datacucu.append(b)
                idcucu.append(b.id)
    for b in idcucu:
        dc=Family.objects.filter(Q(mid=b) | Q(fid=b))
        for c in dc:
            if c != []:
                datacicit.append(c)
                idcicit.append(c.id)
    for d in idcicit:
        dc=Family.objects.filter(Q(mid=d) | Q(fid=d))
        for f in dc:
            if f != []:
                datapiut.append(f)

    anak=dataanak.count()
    cucu=len(datacucu)
    cicit=len(datacicit)
    piut=len(datapiut)

    family=list(Family.objects.values('id','pids','mid','fid','name', 'gender', 'born', 'country', 'city', 'phone','email','photo'))
    family_members=Family.objects.filter(born__month=today.month)
    nearest_birthday = None
    nearest_birthday_diff = 999
    databirthday=[]
    for member in family_members:
        # Get the difference between the member's birthday and today
        birthday_diff = (member.born.replace(year=today.year) - today).days
        person={'name' : member.name, 'sisahari':birthday_diff, 'born':member.born}
        databirthday.append(person)
    new_list = [{k: v for k, v in d.items() if v is not None} for d in family]
    new_list = [{k: ast.literal_eval(v) if k == 'pids' else v for k, v in d.items()} for d in new_list]
    for i in range(len(new_list)):
        for key, value in new_list[i].items():
            if isinstance(value, date):
                new_list[i][key] = value.strftime('%Y-%m-%d')
    for item in new_list:
        if 'photo' in item:
            item['photo'] = 'https://rohimexc.pythonanywhere.com/media/' + item['photo']
    context={
        'data': json.dumps(new_list),
         'databirthday': databirthday,
         'anak':anak,
         'cucu':cucu,
         'cicit':cicit,
         'piut':piut,
         }
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

@user_passes_test(lambda u: u.is_superuser)
def register(request):
    optionfamily=Family.objects.all()
    if request.method == "POST":
        form = NewUserForm(request.POST)
        idUser=request.POST.get('username')
        foto_profil=Family.objects.get(id=idUser)
        photo=""
        newusername="huseinfamily@"+idUser
        print(newusername)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.username=newusername
            instance.save()
            messages.success(request, "Registration successful." )
            try:
                user=User.objects.get(username=newusername)
            except:
                messages.error(request, "Beluum ada User")
            if foto_profil.photo:
                photo=foto_profil.photo
            if user:
                buat_profil=Profile.objects.create(
                    user=user,
                    profil=photo
                )
                buat_profil.save()
            return redirect("akun")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    context={'form':form, 'optionfamily':optionfamily}
    return render (request, 'family_app/register.html',context)


@user_passes_test(lambda u: u.is_superuser)
def hapus_akun(request, id_user):
    user=User.objects.get(id=id_user)
    if request.method=='POST':
        user.delete()
    return redirect("akun")

@login_required(login_url='login')
def navbar(request):
    user=request.user
    try:
        profil=Profile.objects.get(user=user)
        photo='./media/' + profil.profil
    except:
        photo='./static/img_2/profile-img.jpg'
    print(photo)
    context={'photo':photo}
    return render(request,'family_app/navbar.html',context)

@login_required(login_url='login')
def admin(request):
    family_members=Family.objects.filter(born__month=today.month)
    user=request.user
    if "@" in str(user):
        id_user=str(user).split('@')[1]
    else:
        id_user=17
    anak=0
    cucu=0
    cicit=0
    piut=0
    datacucu=[]
    datacicit=[]
    datapiut=[]
    idanak=[]
    idcucu=[]
    idcicit=[]
    idpiut=[]

    dataanak=Family.objects.filter(Q(mid=id_user) | Q(fid=id_user))
    for a in dataanak:
        idanak.append(a.id)
    menantu_anak=Family.objects.filter(Q(pids__in=idanak)).count()
    for a in idanak:
        dc=Family.objects.filter(Q(mid=a) | Q(fid=a))
        for b in dc:
            if b != []:
                datacucu.append(b)
                idcucu.append(b.id)
    menantu_cucu=Family.objects.filter(Q(pids__in=idcucu)).count()
    for b in idcucu:
        dc=Family.objects.filter(Q(mid=b) | Q(fid=b))
        for c in dc:
            if c != []:
                datacicit.append(c)
                idcicit.append(c.id)
    menantu_cicit=Family.objects.filter(Q(pids__in=idcicit)).count()
    for d in idcicit:
        dc=Family.objects.filter(Q(mid=d) | Q(fid=d))
        for f in dc:
            if f != []:
                datapiut.append(f)
                idpiut.append(f.id)
    menantu_piut=Family.objects.filter(Q(pids__in=idpiut)).count()

    anak=dataanak.count()
    anak=anak+menantu_anak
    cucu=len(datacucu)+menantu_cucu
    cicit=len(datacicit)+menantu_cicit
    piut=len(datapiut)+menantu_piut
    nearest_birthday = None
    nearest_birthday_diff = 999
    databirthday=[]
    for member in family_members:
        # Get the difference between the member's birthday and today
        birthday_diff = (member.born.replace(year=today.year) - today).days
        person={'name' : member.name, 'sisahari':birthday_diff, 'born':member.born}
        databirthday.append(person)

    family=list(Family.objects.values('id','pids','mid','fid','name', 'gender', 'born','death', 'country', 'city', 'phone','email','photo'))
    new_list = [{k: v for k, v in d.items() if v is not None} for d in family]
    new_list = [{k: ast.literal_eval(v) if k == 'pids' else v for k, v in d.items()} for d in new_list]
    for item in new_list:
        if 'photo' in item:
            item['photo'] = 'https://rohimexc.pythonanywhere.com/media/' + item['photo']

    for i in range(len(new_list)):
        for key, value in new_list[i].items():
            if isinstance(value, date):
                new_list[i][key] = value.strftime('%Y-%m-%d')
    context={
        'data': json.dumps(new_list),
         'databirthday':databirthday,
          'anak':anak,
          'cucu':cucu,
          'cicit':cicit,
          'piut':piut,
          }
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
    optionfamily=Family.objects.all()
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
            relation_idf=request.POST.get('relation_from')
            if relation == 'suami' or  relation == 'istri':
                instance.pids=[int(relation_idf)]
                instance.city=city
                instance.country=country
                instance.save()
                optionFamilyGet=Family.objects.get(id=relation_idf)
                if optionFamilyGet.pids != None:
                    parsed_list = ast.literal_eval(optionFamilyGet.pids)
                    parsed_list.append(instance.id)
                    optionFamilyGet.pids = parsed_list
                    optionFamilyGet.save()
                else:
                    optionFamilyGet.pids = [instance.id]
                    optionFamilyGet.save()

            elif relation == 'anak perempuan' or  relation == 'anak laki-laki':
                instance.fid=relation_idf
                pasangan=ast.literal_eval(Family.objects.get(id=relation_idf).pids)

                instance.mid=pasangan[0]
                instance.city=city
                instance.country=country
                instance.save()
            else:
                instance.city=city
                instance.country=country
                instance.save()
                gender=form.cleaned_data['gender']

                optionFamilyGet=Family.objects.get(id=relation_idf)
                if gender == 'male':
                    optionFamilyGet.mid=instance.id
                else:
                    optionFamilyGet.fid=instance.id
                optionFamilyGet.save()

            messages.success(request,'Berhasil Simpan Data')

            return redirect('database')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form, 'city':citydb, 'country':countrydb, 'optionfamily':optionfamily}
    return render(request, 'family_app/tambah_keluarga.html',context)

@login_required(login_url='login')
def hapusKeluarga(request,id):
    family=Family.objects.get(id=id)
    if request.method == "POST":
        family.delete()
        messages.success(request, 'Data berhasil dihapus')
    return redirect('database')

@login_required(login_url='login')
def editKeluarga(request,id):
    ins_family=Family.objects.get(id=id)
    citydb=OptionCity.objects.all()
    countrydb=OptionCountry.objects.all()
    optionfamily=Family.objects.all()
    form = Familyform(instance=ins_family)
    for row in OptionCity.objects.all().reverse():
        if OptionCity.objects.filter(city=row.city).count() > 1:
            row.delete()
    for row in OptionCountry.objects.all().reverse():
        if OptionCountry.objects.filter(country=row.country).count() > 1:
            row.delete()
    if request.method=='POST':
        form=Familyform(request.POST,request.FILES,instance=ins_family)
        if form.is_valid():
            form.save()
            messages.success(request,'Berhasil Update Data')
            return redirect('database')
        else:
            messages.warning(request, "Pastikan Mengisi Semua data yang diminta")
    context={'form':form,}
    return render(request, 'family_app/edit_keluarga.html',context)

@login_required(login_url='login')
def report(request):
    family=Family.objects.all()
    user=request.user
    if "@" in str(user):
        id_user=str(user).split('@')[1]
    else:
        id_user=17
    def anak(ids=id_user,jk=['male','female']):
        family=Family.objects.filter(Q(mid=ids)|Q(fid=ids)).filter(gender__in=jk)
        return family
    def cucu(ids=id_user,jk=['male','female']):
        anak=Family.objects.filter(Q(mid=ids)|Q(fid=ids)).filter(gender__in=jk)
        idcucu=[]
        for a in anak:
            idcucu.append(a.id)
        family=Family.objects.filter(Q(mid__in=idcucu)|Q(fid__in=idcucu)).filter(gender__in=jk)
        return family
    def cicit(ids=id_user,jk=['male','female']):
        anak=Family.objects.filter(Q(mid=ids)|Q(fid=ids)).filter(gender__in=jk)
        idcucu=[]
        idcicit=[]
        for a in anak:
            idcucu.append(a.id)
        cucu=Family.objects.filter(Q(mid__in=idcucu)|Q(fid__in=idcucu)).filter(gender__in=jk)
        for a in cucu:
            idcicit.append(a.id)
        family=Family.objects.filter(Q(mid__in=idcicit)|Q(fid__in=idcicit)).filter(gender__in=jk)
        return family
    tingkat = request.POST.get('tingkat')
    keluarga = request.POST.get('keluarga')
    jk = request.POST.get('gender')

    if tingkat == 'anak':
        if keluarga:
            if jk:
                family = anak(keluarga, [jk])
            else:
                family = anak(keluarga)
        else:
            family = anak()
    elif tingkat == 'cucu':
        if keluarga:
            if jk:
                family = cucu(keluarga, [jk])
            else:
                family = cucu(keluarga)
        else:
            family = cucu()
    elif tingkat == 'cicit':
        if keluarga:
            if jk:
                family = cicit(keluarga, [jk])
            else:
                family = cicit(keluarga)
        else:
            family = cicit()
    else:
        messages.info(request, 'Pilih untuk menfilter')

    context={'family':family}
    return render(request,'family_app/report.html',context)

@login_required(login_url='login')
def akun(request):
    user=User.objects.all()
    context={'user':user}
    return render(request,'family_app/akun.html',context)

