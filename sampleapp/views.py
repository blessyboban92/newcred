from django.contrib import auth, messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.models import User,AbstractUser
from . models import Services
#from django.http import HttpResponse
def demo(request):
    obj=Services.objects.all()
    return render(request,'index.html',{'result':obj})


def customerf(request):
    return render(request, 'customer.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return render(request,'customer.html')
        else:
            messages.info(request,"Invalid credential")
            return redirect('login')
    return render(request,'login.html')

def registerf(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        confirmpassword = request.POST['confirmpassword']
        if password == confirmpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Alreay existed user")
                return redirect('register.html')
            else:
                user = User.objects.create_user(username=username, password=password)
                user.save()
                return redirect('login')
            print("User Created")
        else:
            messages.info(request, "Password does not match")
            return redirect('register')
        return redirect('login.html')
    return render(request,'register.html')


