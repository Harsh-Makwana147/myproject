from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from . import models




def login(request):
    return render(request,"login.html")

def signup(request):
    return render(request,"signup.html")

def home(request):
    return render(request,"home.html")

def test(request:HttpRequest):
    data = models.Role.objects.all()
    admin_role=models.Role()
    admin_role.name="admin"
    admin_role.save()
    return HttpResponse("Role created successfully!")
