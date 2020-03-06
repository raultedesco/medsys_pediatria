from django import forms
from django.forms import ModelForm
from django.forms.models import model_to_dict
from .models import turno


class DateInput(forms.DateTimeInput):
    input_type = 'datetime'


class TurnoForm(ModelForm):

    fecha_turno = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])

    class Meta:
     model = turno
    #  fields = ['dni', 'nya', 'fecha_nac']
     fields = '__all__'
     fields = ['fecha_turno', 'nya','paciente_id','tratado']
    #  widgets = {
    #   'fecha_turno': DateInput(),
    # #   'paciente_id': forms.HiddenInput()
    #  }


