from django import forms
from .models import Sprinkler, Plan

class SprinklerForm(forms.ModelForm):
    class Meta:
        model = Sprinkler
        fields = '__all__'

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'
    
