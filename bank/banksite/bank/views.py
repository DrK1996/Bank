from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .models import District, Branch

def homepage(request):
    return render(request, 'homepage.html')

def application_submit(request):
    # Your submission logic goes here
    return render(request, 'submission_success.html')


def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('new_page')
        else:
            messages.info(request,"Invalid User")
            return redirect('login')
    return render(request, 'login.html')

def register_page(request):
    if request.method == 'POST':
        username=request.POST['username']
        pwd = request.POST['password1']
        cpwd = request.POST['password2']
        if pwd==cpwd:
            if User.objects.filter(username=username).exists():
                messages.info(request,"Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=pwd)
                user.save();
                return redirect('login')
        else:
            messages.info(request,"Password Not Matched")
            return redirect('register')
        return redirect('/')
    return render(request, 'register.html')

def new_page(request):
    return render(request, 'new_page.html')


def form_page(request):
    districts = District.objects.all()
    branches = Branch.objects.all()

    if request.method == 'POST':
        message = "Application accepted"
    else:
        message = None
    return render(request, 'form_page.html', {'message': message, 'districts': districts, 'branches': branches})

def logout(request):
    auth.logout(request)
    return redirect('/')
