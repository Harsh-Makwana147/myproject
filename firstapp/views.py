from pyexpat import model
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest, response
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

def print(request:HttpRequest):
    data=models.Role.objects.all()
    result = "<br>".join([str(role) for role in data])
    return HttpResponse(result)
    
def dele(request:HttpRequest):
    ans=models.Role.objects.all()
    ans.delete()
    return HttpResponse("delete succesfully")

