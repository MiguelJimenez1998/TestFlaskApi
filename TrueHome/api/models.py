from django.db import models

# Create your models here.
class Adress (models.Model):
    id = models.AutoField(primary_key=True)
    street=models.TextField(null=True, blank=True)
    number=models.TextField(null=True, blank=True)
    settlement=models.TextField(null=True, blank=True)
    town=models.TextField(null=True, blank=True)
    state=models.TextField(null=True, blank=True)
    country=models.TextField(null=True, blank=True)

class House (models.Model):
    id = models.AutoField(primary_key=True)
    name=models.TextField(blank=True)
    price=models.TextField(blank=True)
    adress=models.ForeignKey(Adress,on_delete=models.CASCADE)
    description=models.TextField(blank=True)
    amenities=models.TextField(blank=True)
    size=models.TextField(blank=True)
    picture=models.TextField(blank=True)


