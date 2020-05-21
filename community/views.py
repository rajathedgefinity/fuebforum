from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate

# Create your views here.

def index(request):
    return render(request, 'community/forum-landing.html')

def login_forum(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('login')
    return render(request, 'community/forum-login.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def faq(request):
    return render(request, 'community/faq.html')

def forum_thread(request):
    return render(request, 'community/forum-thread.html')

def profile(request):
    return render(request, 'community/profile.html')

def profile_settings(request):
    return render(request, 'community/profile-setting.html')
