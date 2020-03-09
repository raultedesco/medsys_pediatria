from django import forms
from django.forms import ModelForm
from django.forms.models import model_to_dict
from .models import Afiliado


class DateInput(forms.DateInput):
    input_type = 'date'


class AfiliadoForm(ModelForm):

    class Meta:
     model = Afiliado
    #  fields = ['dni', 'nya', 'fecha_nac']

     fields = ['nya', 'n_afiliado','ObraSocial','paciente_id']
     widgets = {
      'paciente_id': forms.HiddenInput()
     }

class AfiliadoDetailForm(ModelForm):

    def __init__(self, *args, **kwargs):
       super(AfiliadoDetailForm, self).__init__(*args, **kwargs)
       fields = Afiliado._meta.get_fields()
  
    #    other way to code change with more lines
     
       self.fields['nya'].widget.attrs['readonly'] = True
       self.fields['n_afiliado'].widget.attrs['readonly'] = True
    
    class Meta:
        model=Afiliado
        fields='__all__'
