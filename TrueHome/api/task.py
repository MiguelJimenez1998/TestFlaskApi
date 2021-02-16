from celery import shared_task
from api.models import *

@shared_task()

def save_db(num_houses:int):
    #num=int(request.POST["numero"])
    data=scrapy(num_houses)
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

    return "Task complete"