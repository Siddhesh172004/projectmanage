from django.shortcuts import render,redirect
from django.http.response import HttpResponse
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate , login ,logout
from . models import Contact
# Create your views here.
def homepage(request):
    return render(request,'Home1/HomeC.html')

def signup(request):
    return render(request,'Home1/signup.html')

def signview(request):
    if request.method == "POST":
        username = request.POST.get("username")
        email= request.POST.get("email")
        pass1= request.POST.get("pass1")
        pass2= request.POST.get("pass2")
        f_name = request.POST.get("first_name")
        last_name= request.POST.get("last_name")
        
        # validationssssss
        if (User.objects.filter(username=username).exists()): 
            messages.add_message(request, messages.INFO, 'Username already exist.')
            return redirect("/signup/")           
            

        if(not(len(pass1)>7 and not pass1.isalnum())):
            messages.add_message(request, messages.INFO, 'Password must belonger then 8 characters and should contain a symbol.')
            return redirect("/signup/")
        
        if(not(pass1==pass2)):
            messages.add_message(request, messages.INFO, 'Both the password must be same.')
            return redirect("/signup/")

        else:
            try:
                newUser = User.objects.create_user(username,email,pass1)
                newUser.first_name = f_name
                newUser.last_name = last_name
                newUser.save()
                messages.add_message(request, messages.SUCCESS, 'Account succsessfully Created. Please Login to continue.')
                return redirect("/login/")
            except Exception as e:
                messages.add_message(request, messages.ERROR, e)
                return redirect("/signup/")            
    else:
        messages.add_message(request, messages.ERROR, 'Please SignIn.')
        return redirect("/login/")




def loginkaro(request):
    return render(request,'Home1/login.html')

def logindone(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("pass")
        
        user = authenticate(username = username , password = password )

        if user is not None:
            login(request,user)
            messages.add_message(request, messages.SUCCESS, 'LOGIN successfull!!')
            return redirect("/")

        else:
            messages.add_message(request, messages.ERROR, 'Email or password is not valid. ')
            return redirect("/login/")
    else:
        messages.add_message(request, messages.ERROR, 'Please Login.')
        return redirect("/login/")
    
def logoutkaro(request):
    logout(request)
    messages.add_message(request, messages.SUCCESS, 'Logout successful')
    return redirect("/")

def contactus(request):
    return render(request,'Home1/contact.html')   

def Contactsubmit(request):
    email=request.POST.get("email")
    name=request.POST.get("name")
    phone=request.POST.get("phone")
    desc=request.POST.get("desc")
    image1=request.FILES['screenshot']
    selfcontact=Contact(Name=name,Email=email,Tel=phone,Image=image1,Desc=desc)
    selfcontact.save()
    return HttpResponse("<h1>thanks for the response</h1><a href='/shop'>")
   