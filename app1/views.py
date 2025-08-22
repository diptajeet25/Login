from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.contrib import messages
from django.http import HttpResponse  # Import HttpResponse here

def HomePage(request):
    return render(request, 'home.html')

from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages

def SignupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        # Check if passwords match
        if pass1 != pass2:
            messages.error(request, "Your Password & Confirm password do not match!")
            return render(request, 'signup.html')

        # Check if username already exists
        if User.objects.filter(username=uname).exists():
            messages.error(request, "Username already exists!")
            return render(request, 'signup.html')

        # Check if email already exists
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists!")
            return render(request, 'signup.html')

        # Create the new user
        my_user = User.objects.create_user(username=uname, email=email, password=pass1)
        my_user.save()

        # Show success message and redirect to login
        messages.success(request, "Account created successfully! Please log in.")
        return redirect('login')

    return render(request, 'signup.html')


def LoginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        
        if user is not None:
            login(request, user)
            return redirect('home') 
        else:
            return HttpResponse("Username or Password is incorrect")  # Correct indentation for incorrect login
    
    return render(request, 'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')
