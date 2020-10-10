from django.shortcuts import render
from django.http import HttpResponse
from Covid19.models import *
# Create your views here.


'''
def home(req):
    return render(req,"Covid19/home.html")
   # return HttpResponse("<center><h1><strong>Hello I am </strong></h1><center>")

def home(req,user,age,sex):
    return HttpResponse("Hello , This is " +user+ "My age is " +age+ " My gender is" +gender)
'''
def home(req):
    data = {"name":"siva","age":20}
    return render(req,"Covid19/home.html",{"data":data})

def register(req):
    if req.method=="POST":
        name = req.POST['uname']
        age = req.POST['age']
        email = req.POST['pemail']
        data= Patients.objects.create(P_name=name,P_age=age,P_email=email)
        return HttpResponse("data added successfully")
        return render(req,"Covid19/register.html")

        #data=Patients.objects.



def about(req,user,des):
    return HttpResponse("Hello Mr."+user+" "+des)

def welcome(req):
    return render(req,"Covid19/welcome.html")