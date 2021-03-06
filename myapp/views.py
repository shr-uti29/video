from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from .models import Profile
from django.contrib import messages

# Create your views here.
# def index(request):
#     return render(request,"index.html")

def login(request):
    #return render(request,'room.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('room')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')
    else:
        return render(request,'index.html')

# def main(request):
#     return render(request,'main.html',{'name':request.user.get_username()})

def register(request):
    
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        Contact = request.POST['Contact']
        
        

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email already registered')
                return redirect('register')
            else:     
                user= User.objects.create_user(username=username,password=password1,first_name=first_name,last_name=last_name,email=email)
                user.save()
                prof=Profile(user=user,Contact=Contact)
                prof.save()
                print('user created')
                return redirect('room')
        else:
            messages.info(request,'Password not matching')
            return redirect('register')
        return redirect('room')
    else:
        return render(request,'register.html')

def room(request):
    return render(request,"room.html")

def logout(request):
    auth.logout(request)
    return redirect('register')

