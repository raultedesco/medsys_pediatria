from django import forms
from django.forms import ModelForm
from django.forms.models import model_to_dict
from .models import vacuna, vacuna_periodo, vacuna_tipo


class DateInput(forms.DateInput):
    input_type = 'date'


class VacunaForm(ModelForm):

    class Meta:
     model = vacuna
    #  fields = ['dni', 'nya', 'fecha_nac']
     fields = '__all__'
     fields = ['fecha_aplicacion', 'periodo_id','tipo_id','paciente_id']
     widgets = {
      'fecha_aplicacion': DateInput(),
      'paciente_id': forms.HiddenInput()
     }


# class AfiliadoDetailForm(ModelForm):

#     def __init__(self, *args, **kwargs):
#        super(AfiliadoDetailForm, self).__init__(*args, **kwargs)
#        fields = Afiliado._meta.get_fields()
  
#     #    other way to code change with more lines
     
#        self.fields['nya'].widget.attrs['readonly'] = True
#        self.fields['n_afiliado'].widget.attrs['readonly'] = True
    
#     class Meta:
#         model=Afiliado
#         fields='__all__'
