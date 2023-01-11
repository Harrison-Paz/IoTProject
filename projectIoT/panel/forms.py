from django import forms
from .models import Sprinkler, Plan

class SprinklerForm(forms.ModelForm):
    class Meta:
        model = Sprinkler
        fields = '__all__'

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = ['startTime', 'endTime', 'sprinkler']
    Sprinkler = forms.ModelChoiceField(queryset=Sprinkler.objects.all())
