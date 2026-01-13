from django.shortcuts import render

from django.http import HttpResponse

def home(request):
    return render(request,'index.html')

def usapage(request):
    return render(request,'pages/usa.html')

def userList(request):
    return render(request,'pages/usercreate.html')
