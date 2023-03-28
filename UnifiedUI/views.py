from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def gatekeeper(request, admin_only=False): return None if ((request.user.is_authenticated and request.user.is_staff) if admin_only else request.user.is_authenticated) else redirect('home', {'Forbidden': True}) 

def home(request): return render(request, 'login.html')
