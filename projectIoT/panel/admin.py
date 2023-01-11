from django.contrib import admin
from .models import Sprinkler, Plan

# Register your models here.
admin.site.register([Sprinkler, Plan])