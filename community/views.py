from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import permission_required, login_required
from django.contrib.auth import get_user_model
from .models import allthread
from django.core.paginator import Paginator

User = get_user_model()

# Create your views here.

def index(request):
    if request.method == 'POST':
        category = request.POST['category']
        product = request.POST['product']
        topic = request.POST['topic']
        message = request.POST['message']
        # print(category, product, topic, message)
        b = allthread(category=category,product=product,topic=topic,content=message,thread_by=request.user)
        b.save()
        return redirect('index')
    all_entries = allthread.objects.all().order_by('-dateandtime')
    paginator = Paginator(all_entries, 5)
    page = request.GET.get('page')
    all_entries = paginator.get_page(page)
    return render(request, 'community/forum-landing.html',{'all_entries':all_entries})

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

def login_register(request):
    if request.method == 'POST':
        f_name = request.POST['fname']
        l_name = request.POST['lname']
        email = request.POST['email']
        mobile = request.POST['mobile1']
        gender = request.POST['radio_gender']
        password = request.POST['password']
        username = f_name
        # print(f_name, l_name, username, email, mobile, gender, password)
        user = User.objects.create_user(username=f_name, first_name=f_name, last_name=l_name, email=email, mobile=mobile, gender=gender, password=password)
        # print(user)
        user.save()
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return redirect('index')
    return render(request, 'community/forum-register.html')

@login_required(login_url = '/login/')
def logout_user(request):
    logout(request)
    return redirect('index')

def faq(request):
    return render(request, 'community/faq.html')

def forum_thread(request, id):
    # print(id)
    entry = allthread.objects.get(pk=id)
    # print(entry.topic)
    return render(request, 'community/forum-thread.html',{'entry':entry})

@login_required(login_url = '/login/')
def profile(request):
    if request.user.is_authenticated:
        created_threads = allthread.objects.all().filter(thread_by = request.user)
        # print(created_threads)
        paginator = Paginator(created_threads, 2)
        page = request.GET.get('page')
        created_threads = paginator.get_page(page)
    return render(request, 'community/profile.html',{'created_threads':created_threads})

@login_required(login_url = '/login/')
def profile_settings(request):
    return render(request, 'community/profile-setting.html')
