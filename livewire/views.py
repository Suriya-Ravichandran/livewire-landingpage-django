from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.urls import reverse
from .forms import EnrollForm
from .models import StudentProject
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import send_mail

# Create your views here.
def index(request):
    projects= StudentProject.objects.all().order_by('-created_at')[:3]
    return render(request,"index.html",{"projects":projects})

@login_required
def allproject(request):
    projects= StudentProject.objects.all().order_by('-created_at')
    return render(request,"allproject.html",{"projects":projects})
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

@login_required
def enroll(request):
    form=EnrollForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        form.save()
        name=request.POST.get("name")
        phone=request.POST.get("phone")
        email=request.POST.get("email")
        address=request.POST.get("address")
        course=request.POST.get("course")
        sendemail="noreplay@livewire.com"
        subject="You Got a Enquiry in Python course registration"
        message=render_to_string("enquirymail.html",{
                "name":name,
                "phoneno":phone,
                "email":email,
                "course":course,
                "address":address,
            })
        
        subjectthanku="Thank you for Registed Python course at Livewire"
        messagethanku=render_to_string("Thankumail.html",{
                "name":name,
                "course":course
            })
        messages.success(request, "Enroll Sucessfully")
        
        # send_mail(subject,message,sendemail,["rsuriya119@gmail.com",])
        send_mail(subjectthanku,messagethanku,sendemail,[email,])

        return redirect("livewire:enroll")
    else:
        return render(request,'enrollform.html',{"form":form})