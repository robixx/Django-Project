from django.shortcuts import render, redirect

from django.http import HttpResponse
from django.contrib import messages
from .models import UserProfile
from django.contrib.auth.hashers import make_password
def home(request):
    return render(request,'index.html')

def usapage(request):
    return render(request,'pages/usa.html')

def userList(request):
    print("METHOD:", request.method)

    if request.method == "POST":
        print("POST DATA:", request.POST)

        username = request.POST.get("username")
        email = request.POST.get("email")
        mobile_no = request.POST.get("mobileNo")
        gender = request.POST.get("gender")
        password = request.POST.get("password")
        password1 = request.POST.get("password1")

        print("USERNAME:", username)

        if password != password1:
            messages.error(request, "Passwords do not match")
            return redirect("userList")

        try:
            UserProfile.objects.create(
                UserName=username,               
                MobileNumber=mobile_no,
                Gender=gender,
                Status=1,
                Password=make_password(password)
            )
            print("USER SAVED")
        except Exception as e:
            print("ERROR:", e)

        messages.success(request, "User created successfully")
        return redirect("userList")

    return render(request, "pages/usercreate.html")
