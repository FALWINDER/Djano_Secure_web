from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .models import User
from django.contrib.auth import logout


def register_user(request):
    if request.user.is_authenticated:
        login(request, request.user)
        if request.user.role == 'admin':
            return redirect('admin_dashboard')
        else:
            return redirect('user_dashboard')
    elif request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        role = request.POST['role']
        user = User.objects.create_user(username=username, email=email, password=password, role=role)
        return redirect('login_user')
    return render(request, 'users/register.html')

def login_user(request):
    if request.user.is_authenticated:
        login(request, request.user)
        if request.user.role == 'admin':
            return redirect('admin_dashboard')
        else:
            return redirect('user_dashboard')
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            if user.role == 'admin':
                return redirect('admin_dashboard')
            else:
                return redirect('user_dashboard')
        else:
            return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    return render(request, 'users/login.html')

def logout_user(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login_user')
