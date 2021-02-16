from django.shortcuts import render, redirect
from django.http import JsonResponse
from seed import scrapy
from django.views.decorators.csrf import csrf_exempt,csrf_protect #Add this

from .task import save_db




import os, sys
sys.path.append("..")
from api.models import *


@csrf_exempt 
def get_houses_view(request):
    num_houses=int(request.POST["numero"])
    save_db.delay(num_houses)

    return "OK_HOLA"


'''
def save_db(request):
    num=int(request.POST["numero"])
    data=scrapy(int(num))
    print("OK")
    adr=Adress.objects.all()
    adr.delete()

    adr=House.objects.all()
    adr.delete()

    for i in range(len(data)):
        add= Adress.objects.create(
            street= data[i][6][0],
            number= data[i][6][1],
            settlement=data[i][6][2],
            town=data[i][6][3],
            state=data[i][6][4],
            country=data[i][6][5])


        House.objects.create(
            name=data[i][0],
            price=data[i][1],
            adress=add,
            description=data[i][2],
            amenities=data[i][3],
            size=data[i][4],
            picture=data[i][5],
                )

    data = dict()
    data["success"] = ""
    return JsonResponse(data)
    
'''
   


    
def inicio(request):
    
    adress = Adress.objects.all()
    house = House.objects.all()
    return render(
            request,
            "db.html",
            {'Adress': adress,
            'House': house,

             }
        )
