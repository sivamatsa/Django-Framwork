from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

'''
def home(req):
    return render(req,"Covid19/home.html")
   # return HttpResponse("<center><h1><strong>Hello I am </strong></h1><center>")
'''
def home(req,user,age,sex):
    return HttpResponse("Hello , This is " +user+ "My age is " +age+ " My gender is" +sex)

def about(req,user,des):
    return HttpResponse("Hello Mr."+user+" "+des)

