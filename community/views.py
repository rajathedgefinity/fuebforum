from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .models import allthread
from django.core.paginator import Paginator
from django.http import JsonResponse

User = get_user_model()

# Create your views here.


def index(request):
    '''
    This function loads the Landing page Where here we can navigate to each topics that
    has been created for the discussion.

    At the same time once you got redirected from the signin page it'll be redirected here from
    the Signin page with Active User.
    '''
    if request.method == 'POST':
        category = request.POST['category']
        product = request.POST['product']
        topic = request.POST['topic']
        message = request.POST['message']
        # print(category, product, topic, message)
        b = allthread(category=category, product=product, topic=topic, content=message, thread_by=request.user)
        b.save()
        return redirect('index')
    all_entries = allthread.objects.all().order_by('-dateandtime')
    paginator = Paginator(all_entries, 5)
    page = request.GET.get('page')
    all_entries = paginator.get_page(page)
    return render(request, 'community/forum-landing.html', {'all_entries': all_entries})


def closed_issues(request):
    '''
    This Function declaration has made for Listing the total closed issues that have been recorded
    from the Users.
    '''
    all_entries = allthread.objects.all().filter(solved=True).order_by('-dateandtime')
    paginator = Paginator(all_entries, 5)
    page = request.GET.get('page')
    all_entries = paginator.get_page(page)
    return render(request, 'community/forum-landing.html', {'all_entries': all_entries})


def opened_issues(request):
    '''
    This Function declaration has made for Listing the total Opened issues that have been recorded
    from the Users.
    '''
    all_entries = allthread.objects.all().filter(solved=False).order_by('-dateandtime')
    paginator = Paginator(all_entries, 5)
    page = request.GET.get('page')
    all_entries = paginator.get_page(page)
    return render(request, 'community/forum-landing.html', {'all_entries': all_entries})


def counting_opened_issues(request):
    '''
    This Function declaration has made for counting the total Opened and Closed issues that have been recorded
    from the Users.
    '''
    count_entries = allthread.objects.all().filter(solved=False).count()  # noqa
    print(count_entries)
    data = {
        'opened_issues': count_entries
    }
    if request.method == 'GET':
        return JsonResponse(data)
    return JsonResponse(data)


def login_forum(request):
    '''
    This Function declaration is for created for loading Login Page and for Accepting the Credentials, for Login.
    '''
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
    '''
    This Function declaration is for created for loading SignUp Page.
    '''
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


@login_required(login_url='/login/')
def logout_user(request):
    '''
    This Function declaration is for created for logout if their is a Active User and if logged In.
    To Checkout i've been used decorator `@login_required`
    '''
    logout(request)
    return redirect('index')


def faq(request):
    '''
    This Function declaration is created for loading the FAQ[Frequently Asked Questions] Page.
    '''
    return render(request, 'community/faq.html')


def forum_thread(request, id):
    '''
    This is the function which used to open the topic particularly the user clicked on the landing page
    '''
    entry = allthread.objects.get(pk=id)  # noqa
    # print(entry.topic)
    return render(request, 'community/forum-thread.html', {'entry': entry})


@login_required(login_url='/login/')
def profile(request):
    '''
    This function is defined to load the topics created by that particular User. Only If and if user is logged In.
    '''
    if request.user.is_authenticated:
        created_threads = allthread.objects.all().filter(thread_by=request.user)  # noqa
        # print(created_threads)
        paginator = Paginator(created_threads, 2)
        page = request.GET.get('page')
        created_threads = paginator.get_page(page)
    return render(request, 'community/profile.html', {'created_threads': created_threads})


@login_required(login_url='/login/')
def profile_settings(request):
    '''
    This function is defined to load the Profile Settings Page. Only If and if user is logged In.
    '''
    return render(request, 'community/profile-setting.html')
