from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


def home(request):
    return render (request , 'home.html', {'name':'Bhavya'})

def adding(request):
    v1 = int(request.POST['num1'])
    v2 = int(request.POST['num2'])
    res = v1 + v2

    return render(request , 'results.html' , { 'result':res} )