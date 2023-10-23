from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

from customer.models import Customer_info


# Create your views here.
@login_required(login_url='login')
def HomePage(request):
    return render (request,'home.html')

def Signup(request):
    if request.method=='POST':
        uname=request.POST['username']
        email=request.POST['email']
        pass1=request.POST['password1']
        pass2=request.POST['password2']
        full_name=request.POST['FULL Name']
        phone_number=request.POST['Phone Number']
        address=request.POST['address']
        key=request.POST['key']


        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(username=uname,email=email,password=pass1)
            my_user.save()
            new_customer=Customer_info(full_name=full_name,phone_number=phone_number,address=address,key=key)
            new_customer.save()

            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')