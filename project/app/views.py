from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Create your views here.

def dictionary(req):
    d={'name':'abc' , 'age':21 , 'place':'vkm'}
   
    return HttpResponse(d)

def std(req):
    d={'name':'abc' , 'age':21 , 'place':'vkm'}
    return HttpResponse(d)

def fun2(req):
    if req.method=='GET':
        d=student.objects.all()
        s=sample(d,many=True)
        return JsonResponse(s.data,safe=False)


@csrf_exempt
def fun3(req):
    if req.method=='GET':
        d=student.objects.all()
        s=model_serializers(d,many=True)
        return JsonResponse(s.data,safe=False)
    elif req.method=='POST':
        d=JSONParser().parse(req)
        s=model_serializers(data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
