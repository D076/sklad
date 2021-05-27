from django.shortcuts import render, get_object_or_404, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.forms import AuthenticationForm
import json
# from .models import Category, Product
# from .forms import ProductForm

# Create your views here.

# @login_required
def index(request):
    if request.method == 'GET':
        return render(request, 'main/index.html')

