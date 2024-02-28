from django.shortcuts import render, redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User


def home(request):
      return HttpResponse("HOME PAGE")

def create(request):
    print(request.method,'request.method')
    if request.method == 'POST':      
        
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        if username == "" and email == "" and password == "":
            msg="Empty username , email or password not allowed!"
            return render(request, 'create.html',{'msg':msg})
        elif User.objects.filter(email=email).exists():
            msg="Already created"
            return render(request, 'create.html',{'msg':msg})
        else:                
            user = User.objects.create_user(username=username, email=email, password=password)           
            msg='Register successfully'
            return render(request, 'create.html',{'msg':msg})
    else:        
        return render(request, 'create.html')

def retrive(request):
      user=User.objects.all()
      return render(request,'retrive.html',{'user':user})
    
def update(request,pk):
    user=User.objects.get(pk=pk)
    if request.method=="POST":
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.pwd=request.POST['pwd']
        user.email=request.POST['email']
        
        user.save()
        return redirect('retrive')
    else:
        return render(request,'update.html',{'user':user})

def delete(request,pk):
    user=User.objects.get(pk=pk)
    user.delete()
    return redirect('retrive')

