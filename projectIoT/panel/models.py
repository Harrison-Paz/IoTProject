import datetime
from django.utils import timezone
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Sprinkler(models.Model):
    codSprinkler = models.CharField(max_length=8, unique=True)
    description = models.CharField(max_length=50)
    state = models.BooleanField(default=False)
    oldState = models.BooleanField(default=False)
    limit = models.IntegerField(default=80,validators=[
        MaxValueValidator(100),
        MinValueValidator(1)
    ])
    autoOn= models.CharField(max_length=1,default='1')
    autoOff = models.CharField(max_length=1,default='1')

class Plan(models.Model):
    sprinkler = models.ForeignKey(Sprinkler, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

class Log(models.Model):
    user = models.CharField(max_length=150, unique=False)
    description = models.CharField(max_length=150)
    date = models.DateTimeField()