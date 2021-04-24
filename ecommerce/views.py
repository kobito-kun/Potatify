from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .decorators import unauthenticated_user
from .models import *

def mainPage(request):
  context = {}
  return render(request, 'index.html', context)

def payPage(request, amount, user):
  created_order = Order.objects.create(
    total = amount,  
    name = user,
  )
  return redirect(f"/pay/{created_order.id}")

def payPage2(request, order_id):
  disabled = True
  order = Order.objects.get(id=order_id)
  context = {
    'order': order,
    'disabled': True,
  }
  return render(request, 'pay.html', context)