from tkinter import CASCADE

from django.db import models

# Create your models here.
class Userregisters_Model(models.Model):
    userid = models.CharField(max_length=10)
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=10)
    email = models.EmailField(max_length=50)
    phoneno = models.CharField(max_length=10)
    address = models.CharField(max_length=100)

class Userwateranalysis_Model(models.Model):
    uregid= models.ForeignKey(Userregisters_Model,on_delete=models.CASCADE,)
    useridorbillno = models.CharField(max_length=10)
    branch = models.CharField(max_length=20)
    now= models.CharField(max_length=20)
    nol = models.CharField(max_length=10)
    amount = models. IntegerField()
    wpd = models.CharField(max_length=20)
    receipt = models.CharField(max_length=20)
    bookdate = models.DateField(max_length=50)
    deliverydate = models.DateField(max_length=50)


class Userfeedback_Model(models.Model):
    uregsid = models.ForeignKey(Userregisters_Model,on_delete=models.CASCADE,)
    name = models.CharField(max_length=300)
    branches = models.CharField(max_length=50)
    rating = models.CharField(max_length=10)
    mobilenumber = models.CharField(max_length=300)
    sentiment = models.CharField(max_length=300)
    topics = models.CharField(max_length=200)
    feedback = models.CharField(max_length=300)

