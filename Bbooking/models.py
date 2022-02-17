from django.db import models
from django import forms


# Create your models here.
class staff(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=10)


class user(models.Model):
    name = models.CharField(max_length=30)
    number = models.CharField(max_length=20)
    email = models.EmailField()
    password = models.CharField(max_length=20)


class bus(models.Model):
    busname = models.CharField(max_length=30)
    froms = models.CharField(max_length=30)
    to = models.CharField(max_length=30)
    fare = models.IntegerField()
    state = models.CharField(max_length=30)
    date = models.DateTimeField()
    duration = models.IntegerField(max_length=24)
    frequency = models.IntegerField()
    b_id = models.CharField(max_length=30)

class booking(models.Model):
    u_id = models.IntegerField()
    b_id = models.IntegerField(default='')
    pass1 = models.CharField(max_length=300, default='')
    pass2 = models.CharField(max_length=300, default='')
    pass3 = models.CharField(max_length=300, default='')
    pass4 = models.CharField(max_length=300, default='')
    pass5 = models.CharField(max_length=300, default='')
    date = models.DateTimeField()
    rate = models.IntegerField()
    # seats = models.IntegerField()
    date_now = models.DateTimeField(auto_now=True)

class karnataka(models.Model):
    passname = models.CharField(max_length=30,default='')
    froms = models.CharField(max_length=30,default='')
    to = models.CharField(max_length=30, default='')
class Punjab(models.Model):
    passname = models.CharField(max_length=30, default='')
    froms = models.CharField(max_length=30, default='')
    to = models.CharField(max_length=30, default='')
class Andra(models.Model):
    passname = models.CharField(max_length=30, default='')
    froms = models.CharField(max_length=30, default='')
    to = models.CharField(max_length=30, default='')
class TamilNadu(models.Model):
    passname = models.CharField(max_length=30, default='')
    froms = models.CharField(max_length=30, default='')
    to = models.CharField(max_length=30, default='')
class Kerala(models.Model):
    passname = models.CharField(max_length=30, default='')
    froms = models.CharField(max_length=30,default='')
    to = models.CharField(max_length=30,default='')

