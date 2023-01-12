import datetime
from django.utils import timezone
from django.db import models


class Sprinkler(models.Model):
    codSprinkler = models.CharField(max_length=8,unique=True)
    description = models.CharField(max_length=50)
    state = models.BooleanField(default=False)

    def __str__(self):
        return self.codSprinkler

class Plan(models.Model):
    sprinkler = models.ForeignKey(Sprinkler, on_delete=models.CASCADE)
    startTime = models.DateTimeField()
    endTime = models.DateTimeField()

    def __str__(self):
        return f"{self.endTime}"