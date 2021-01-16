from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.http import HttpResponse
from signupApp.models import Signup
from django.contrib.auth.hashers import make_password 
from django.contrib import messages ,auth
from django.contrib.auth import authenticate, login, logout


# Create your views here.
def signup(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        phone = request.POST['phone']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        
        #check for error input
        if password1 == password2:
            
            if User.objects.filter(email=email).exists():
                messages.info(request, "invalid email")
                return redirect('index')

           
            elif User.objects.filter(username=username).exists():
                messages.info(request, "invalid username")
                return redirect('index') 
            else:
                #Save in database
                myuser=Signup(username=username, email=email, phone= phone, password1=password1)
                #hashing password
                myuser.password1 = make_password(myuser.password1)
                myuser.save()


                #create user
                myuser = User.objects.create_user(username, email, password1)
                
                myuser.save()
                messages.info(request, "sucessfully created")
                return redirect('profile')        
        else:
            messages.info(request, "invallid password")
            return redirect('index')
        
        
    return render(request, 'signup/signup.html')

def login(request):
    if request.method == 'POST':
        #get the post parameters
        loginusername = request.POST["username"]
        loginpassword = request.POST["password"]

        myuser = auth.authenticate(username=loginusername, password=loginpassword)

        if myuser is not None:
            auth.login(request, myuser)
           
            return redirect('profile')
        else:
            
            return redirect('signup')   
    else:        
        return render(request, 'signup/login.html')



def profile(request):
    return render(request, 'profile/profile.html')
    

def logout(request):
    auth.logout(request)
    
    return redirect('/')

def index(request):
    return render(request, 'index.html')
