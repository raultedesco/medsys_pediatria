from django import forms
from django.forms import ModelForm
from django.forms.models import model_to_dict
from .models import Paciente


class DateInput(forms.DateInput):
    input_type = 'date'


class PacientesForm(ModelForm):

    class Meta:
     model = Paciente
    #  fields = ['dni', 'nya', 'fecha_nac']
     fields = ['nya', 'dni','telefono','celular','direccion','mail','cp','fecha_nac','peso_nac','eg','talla','pc','apgar','tutor' ]
    #  widgets = {
    #   'fecha_nac': DateInput(),
    #  }


class PacienteDetailForm(ModelForm):

    def __init__(self, *args, **kwargs):
       super(PacienteDetailForm, self).__init__(*args, **kwargs)
       fields = Paciente._meta.get_fields()
       
    #    other way to code change with more lines
     
       self.fields['dni'].widget.attrs['readonly'] = True
       self.fields['nya'].widget.attrs['readonly'] = True
       self.fields['telefono'].widget.attrs['readonly'] = True
       self.fields['celular'].widget.attrs['readonly'] = True
       self.fields['direccion'].widget.attrs['readonly'] = True
       self.fields['mail'].widget.attrs['readonly'] = True
       self.fields['cp'].widget.attrs['readonly'] = True
       self.fields['fecha_nac'].widget.attrs['readonly'] = True
       self.fields['peso_nac'].widget.attrs['readonly'] = True
       self.fields['ciudad'].widget.attrs['readonly'] = True
    
    class Meta:
        model=Paciente
        fields='__all__'
