from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
import json
from .models import Mat, ResponsPerson, OrgList, StorageMat
# from .forms import ProductForm

# Create your views here.


@login_required
def index(request):
    if request.method == 'GET':
        dict = {'mat': Mat.objects.all()}
        return render(request, 'main/index.html', dict)


@login_required
def sprav(request):
    if request.method == 'GET':
        return render(request, 'main/sprav.html')


@login_required
def sprav_mat(request):
    if request.method == 'GET':
        dict = {'mat': Mat.objects.all()}
        return render(request, 'main/sprav_mat.html', dict)


@login_required
def sprav_persons(request):
    if request.method == 'GET':
        dict = {'respons_persons': ResponsPerson.objects.all()}
        return render(request, 'main/sprav_persons.html', dict)


@login_required
def sprav_org(request):
    if request.method == 'GET':
        dict = {'org': OrgList.objects.all()}
        return render(request, 'main/sprav_org.html', dict)


@login_required
def mat_on_skald(request):
    if request.method == 'GET':
        dict = {'mat_on_sklad': StorageMat.objects.all()}
        return render(request, 'main/mat_on_sklad.html', dict)


def login_user(request):
    if request.method == 'GET':
        return render(request, 'main/log_in.html', {'form': AuthenticationForm()})
    elif request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'main/log_in.html',
                          {'form': AuthenticationForm(), 'error': "Неверное имя или пароль"})
        else:
            login(request, user)
            return redirect('index')


@login_required
def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
