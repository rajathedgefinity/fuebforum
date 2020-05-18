from django.shortcuts import render, HttpResponse

# Create your views here.

def index(request):
    return render(request, 'community/forum-landing.html')

def login_forum(request):
    return render(request, 'community/forum-login.html')

def post_login(request):
    return render(request, 'community/forum-post-login.html')

def faq(request):
    return render(request, 'community/faq.html')

def forum_thread(request):
    return render(request, 'community/forum-thread.html')

def profile(request):
    return render(request, 'community/profile.html')

def profile_settings(request):
    return render(request, 'community/profile-setting.html')