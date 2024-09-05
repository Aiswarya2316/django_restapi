from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
from .serializers import *
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
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

@csrf_exempt
def fun4(req,d):
    try:
        demo=student.objects.get(pk=d)
    except student.DoesNotExist:
        return HttpResponse('invalid')
    if req.method=='GET':
        s=model_serializers(demo)
        return JsonResponse(s.data)
    elif req.method=='PUT':
        d=JSONParser().parse(req)
        s=model_serializers(demo, data=d)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data)
        else:
            return JsonResponse(s.errors)
    elif req.method=='DELETE':
        demo.delete()
        return HttpResponse('deleted')
    
@api_view(['GET','POST'])
def fun5(req):
    if req.method=='GET':
        d=student.objects.all()
        s=model_serializers(d,many=True)
        return Response(s.data)
    elif req.method=='POST':
        s=model_serializers(data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)
        
@api_view(['GET','PUT','DELETE'])
def fun6(req,d):
    try:
        demo=student.objects.get(pk=d)
    except:
        return Response(status=status.HTTP_204_NO_CONTENT)
    if req.method=='GET':
        s=model_serializers(demo)
        return Response(s.data)
    elif req.method=='PUT':
        s=model_serializers(demo,data=req.data)
        if s.is_valid():
            s.save()
            return Response(s.data)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    elif req.method=='DELETE':
        demo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class fun7(APIView):
    def get(self,req):
        demo=student.objects.all()
        s=model_serializers(demo,many=True)
        return Response(s.data)
    def post(self,req):
        s=model_serializers(data=req.data)
        if s.is_valid():
            s.save()
            return JsonResponse(s.data,status=status.HTTP_201_CREATED)
        else:
            return JsonResponse(s.errors,status=status.HTTP_400_BAD_REQUEST)
        
class fun8(APIView):
    def get(self,req,id):
        try:
            demo=student.objects.get(pk=id)
            s=model_serializers(demo)
            return Response(s.data)
        except student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def put(self,req,id):
        try:
            demo=student.objects.get(pk=id)
            s=model_serializers(demo,data=req.data)
            if s.is_valid():
                s.save()
                return Response(s.data)
            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
        except student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    def delete(self,req,id):
        try:
            demo=student.objects.get(pk=id)
            demo.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except student.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)        