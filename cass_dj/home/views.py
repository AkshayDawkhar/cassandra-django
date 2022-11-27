from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.
def homes(requset):
    return render(requset, 'home.html')


@api_view(['GET', 'POST'])
def hoemapi(request):
    dis = {
        'name': 'akshay',
        'roll_no': 12
    }
    if request.method == 'GET':
        print("you hit GET request")
    if request.method == 'POST':
        data = request.data
        print("you hit POST request")
        print(data)
    return Response(data)


@api_view(['GET', 'POST'])
def finalapi(request):
    dis = dict(name='iteam1', instock=12)
    if request.method == 'GET':
        print("successfully called GET")
    return Response(dis)
