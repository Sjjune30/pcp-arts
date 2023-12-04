from django.contrib import messages
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
def signup(request):
    if request.method == 'POST':
        username = request.POST['Username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['password2']
        if password == confirm_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Already Exists !')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Already Exists !')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,email=email,password=password)
                user.save();
                return redirect('login')
        else:
            messages.info(request,'PASSWORD VARIFICATION FAILED!')
            return redirect('signup')
    return render(request,'register_form.html')