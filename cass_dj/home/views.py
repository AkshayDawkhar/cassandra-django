import json
# from cassandra.cqlengine
from django.http import JsonResponse
from django.core import serializers
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from home import tryingjson

# Create your views here.
def homes(requset):
    return render(requset, 'home.html')


@api_view(['GET', 'POST'])
def hoemapi(request):
    # dis = {
    #     'name': 'akshay',
    #     'roll_no': 12
    # }
    # if request.method == 'GET':
    #     print("you hit GET request")
    # if request.method == 'POST':
    #     data = request.data
    #     print("you hit POST request")
    #     print(data)
    print(tryingjson.getit())
    return Response(tryingjson.getit())


@api_view(['GET', 'POST'])
def finalapi(request):
    # dis = [{'name': 'iteam1', 'instock': 12}, {'name': 'iteam2', 'instock': 13}, ]
    # dis_s= serializers.serialize('json',dis)
    # dis_d = dict(dis)
    # diss = dict(name='iteam0', instock=100)
    if request.method == 'POST':
        data=request.data
        print(data,type(data))
        print( "successfully called POST")
        return Response(tryingjson.addit(data))
    return Response({})