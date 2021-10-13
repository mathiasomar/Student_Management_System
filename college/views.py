from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.

def adminPage(request):
    return render(request, 'index.html')

def adminLogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        pass1 = request.POST['password']

        user = auth.authenticate(username=username, password=pass1)

        if user is not None:
            auth.login(request, user)
            return redirect('/admin_home')
        else:
            messages.info(request, "Invalid Credentials")
            return redirect('/adminLogin')
    else:
        return render(request, 'login.html')

def staffLogin(request):
    return render(request, 'staffLogin.html')

def studentLogin(request):
    return render(request, 'studentLogin.html')

def adminRegister(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        pass1 = request.POST['password1']
        pass2 = request.POST['password2']

        if pass1 == pass2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('/adminRegister')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "Email Taken")
                return redirect('/adminRegister')
            else:
                user = User.objects.create_user(username=username,email=email, password=pass1)
                user.save()
                return redirect('/adminLogin')
        else:
            messages.info(request, "Password do not match")
            return redirect('/adminRegister')
    else:
        return render(request, 'register.html')

def staffRegister(request):
    return render(request, 'staffRegister.html')

def studentRegister(request):
    return render(request, 'studentRegister.html')

def adminLogout(request):
    auth.logout(request)
    return redirect('/adminLogin')

def staffLogout(request):
    auth.logout(request)
    return redirect('/staffLogin')

def studentLogout(request):
    auth.logout(request)
    return redirect('/studentLogin')
