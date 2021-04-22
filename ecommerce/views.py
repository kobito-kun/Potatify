from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from .models import *

def mainPage(request):
  products = Product.objects.all()
  context = {
    'products': products
  }
  return render(request, 'index.html', context)

def individualPage(request, title):
  product = Product.objects.get(title=title)
  context = {
    'product': product
  }
  return render(request, 'product.html', context)

def payPage(request, id):
  product = Product.objects.get(id=id)
  context = {
    'product': product
  }
  return render(request, 'pay.html', context)