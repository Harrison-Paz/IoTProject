from django import forms
from django.forms import ValidationError,fields
from .models import Sprinkler, Plan

class SprinklerForm(forms.ModelForm):
    
    class Meta:
        model = Sprinkler
        fields = '__all__'

    def clean(self):
        super(SprinklerForm,self).clean()

        codigo = self.cleaned_data.get('codSprinkler')
        descripcion = self.cleaned_data.get('description')

        if(codigo == None):
            self._errors['codSprinkler'] = self.error_class(['El código no puede estar en blanco'])
        else:
            if(descripcion == None):
                self._errors['codSprinkler'] = self.error_class(['La descripción no puede estar en blanco'])
            else:
                try:
                    sprinkler = Sprinkler.objects.get(codSprinkler=codigo)
                except Sprinkler.DoesNotExist:
                    sprinkler = None
                if (sprinkler is not None):
                    self._errors['codSprinkler'] = self.error_class(['El código proporcionado ya existe.'])

        return self.cleaned_data

class PlanForm(forms.ModelForm):
    class Meta:
        model = Plan
        fields = '__all__'

    def clean(self):
        super(PlanForm,self).clean()

        id = self.cleaned_data.get('sprinkler')
        inicio = self.cleaned_data.get('startTime')
        fin = self.cleaned_data.get('endTime')

        print(id)
        plans = Plan.objects.all()

        if (id == "-1" or id == None):
            self._errors['sprinkler'] = self.error_class(['Recuerde seleccionar un aspersor.'])

        if (inicio>fin):
            self._errors['sprinkler'] = self.error_class(['La fecha de inicio no puede ser mayor que la de finalización.'])
        else:
            for plan in plans:
                pId = plan.sprinkler
                pStart = plan.startTime
                pEnd = plan.endTime

                if (pId == id):
                    if not (((inicio < pStart) and (fin < pStart)) or ((inicio > pEnd) and (fin > pEnd ))):
                        self._errors['sprinkler'] = self.error_class(['La fecha interfiere con otra ya programada.'])

        return self.cleaned_data

class SprinklerFormEdit(forms.ModelForm):
    
    class Meta:
        model = Sprinkler
        fields = ['id','codSprinkler','description','limit','autoOn','autoOff']

    def clean(self):
        super(SprinklerFormEdit,self).clean()

        return self.cleaned_data
