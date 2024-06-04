from django.shortcuts import render,redirect
from django.contrib.auth import authenticate, login, logout
from .models import User
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginpage(request):
    context={
        'error':""
        }
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('/orders/customers/')
        else:
            context={
            'error':"*Invalid username or password"
            }
            return render(request,'login.html',context)
            
            
    return render(request,'login.html',context)

def logout_user(request):
    logout(request)
    return redirect('/')

def signup(request):
    context={
        "error":""
    }

    if request.method=="POST":
        check_user=User.objects.filter(username=request.POST['username'])
        if len(check_user) > 0 :
            context={
                "error":"*User name already exits"
            }
            return render(request,'signup.html',context)
        
        else:
            user_name=request.POST.get('username')
            password=request.POST.get('password')
            last_name=request.POST.get('username')
            first_name=request.POST.get('username')
            age=request.POST.get('age')

            new_user=User(username=user_name ,first_name=first_name, last_name=last_name ,age=age)
            new_user.set_password(password)
            new_user.save()
            return redirect('/')


    return render(request,'signup.html',context)

@login_required(login_url="logout")
def home(request):
    return render(request,'customers.html')