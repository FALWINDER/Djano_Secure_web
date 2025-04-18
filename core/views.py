from django.shortcuts import  redirect
from django.contrib.auth import login

def redirect_to_login(request):
    if request.user.is_authenticated:
        login(request, request.user)
        if request.user.role == 'admin':
            return redirect('dashboard/admin-dashboard')
        else:
            return redirect('dashboard/user-dashboard')
    return redirect('login_user')