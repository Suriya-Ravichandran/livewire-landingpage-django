from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def index(request):
    return render(request,"index.html")


def about(request):
    return render(request,"about.html")


def oldurl(request):
    return redirect(reverse("livewire:newurl"))

def newurl(request):
    return HttpResponse("This new url")

def signin(request):
    if request.method=='POST':
        username=request.POST.get("name")
        password=request.POST.get("password")
        user= authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect("livewire:index")
        else:
            messages.error(request, "Invaild User or Password")
            return redirect("livewire:signin")
    return render(request,'signin.html')

def signup(request):
    if request.method=='POST':
        username=request.POST.get("name")
        email=request.POST.get("email")
        password=request.POST.get("password")
        confirmpassword=request.POST.get("confirmpassword")
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect("livewire:signup")
        if password!=confirmpassword:
            messages.error(request, "Password Not Match")
            return redirect("livewire:signup")
        # 2️⃣ Create the user in auth_user table
        User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        messages.success(request, "Signup successful! Go to login...")
        return redirect("livewire:signup")
    
    return render(request,'signup.html')

def signout(request):
    logout(request)
    return redirect("livewire:index")