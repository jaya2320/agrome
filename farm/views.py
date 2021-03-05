from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.models import User,auth
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request,'index.html')

def login(request):
    return render(request,'login.html')

@login_required(login_url='index')
def news(request):
    return render(request,'news.html')

@login_required(login_url='index')
def dealer(request):
    return render(request,'our-product.html')

@login_required(login_url='index')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='index')
def shop(request):
    return render(request,'shop.html')

def signup(request):
    return render(request,'signup.html')

@csrf_exempt
def enter(request):
    if request.method=='POST':
        username=request.POST['username']
        
        pass1=request.POST['pass1']
        user=auth.authenticate(username=username,password=pass1)
        if user is not None:
            auth.login(request,user)
            return render(request,'index.html')
        else:
            messages.info(request,'Invalid credentials')
            return render(request,'login.html')

    else:
        
        return render(request,'login.html')

@csrf_exempt
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        
        if pass1==pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'OOPS! Usename already taken')
                return render(request,'signup.html')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'OOPS! Email already taken')
                return render(request,'signup.html')
            else:
                user=User.objects.create_user(username=username,email=email,password=pass1)
                user.save()
                messages.info(request,'Account created successfully!!')
                return render(request,'login.html')
        else:
            messages.info(request,'Password do not match')
            return render(request,'signup.html')

    else:
        return render(request,'signup.html')

def logout(request):
    auth.logout(request)
    return render (request,'index.html')

@login_required(login_url='index')
def edit(request):
    return render(request,'edit.html')