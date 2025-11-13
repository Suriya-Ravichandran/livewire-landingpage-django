from django.shortcuts import render,HttpResponse,redirect
from django.urls import reverse

# Create your views here.
def index(request):
    
    title="Home-Livewire"
    content="Index page"

    context={
        "title":title,
        "content":content,
    }
    return render(request,"index.html",context)


def about(request):
    title="About-Livewire"

    context={
        "title":title,
    }

    return render(request,"about.html",context)


def oldurl(request):
    return redirect(reverse("livewire:newurl"))

def newurl(request):
    return HttpResponse("This new url")

def signin(request):
    title="signin"

    context={
        "title":title
    }
    return render(request,'signin.html',context)

def signup(request):
    title="signup"

    context={
        "title":title
    }
    return render(request,'signup.html',context)