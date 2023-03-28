from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

def gatekeeper(request, admin_only = False): return None if ((request.user.is_authenticated and request.user.is_staff) if admin_only else request.user.is_authenticated) else redirect('home', {'Forbidden': True})  

def authenticator(request):
    if request.user.is_authenticated: return home(request)
    username, password = request.POST.get('username'), request.POST.get('password')
    userauth = authenticate(request, username=username, password=password)
    if userauth: login(request, userauth); return redirect('home')
    return render(request, 'login.html', {'Forbidden': True})


# def home(request):
#     pass