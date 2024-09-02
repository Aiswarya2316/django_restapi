from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def dictionary(req):
    d={'name':'abc' , 'age':21 , 'place':'vkm'}
   
    return HttpResponse(d)

def std(req):
    d={'name':'abc' , 'age':21 , 'place':'vkm'}
    return HttpResponse(d)
