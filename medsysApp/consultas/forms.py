from django import forms
from django.forms import ModelForm
from django.forms.models import model_to_dict
from .models import Consulta


class DateInput(forms.DateInput):
    input_type = 'date'


class ConsultaForm(ModelForm):

    class Meta:
     model = Consulta
    #  fields = ['dni', 'nya', 'fecha_nac']
    #  fields = '__all__'
     fields = ['peso', 'perimetro_encef','talla','ap','descripcion','paciente']
     widgets = {
       'ap': DateInput(),
       'descripcion': forms.Textarea(attrs={'placeholder': u'Ingrese Texto de la Consulta'}),
       'paciente': forms.HiddenInput()
     }

class ConsultaUpdateForm(ModelForm):

    class Meta:
     model = Consulta
    #  fields = ['dni', 'nya', 'fecha_nac']
    #  fields = '__all__'
     fields = ['peso', 'perimetro_encef','talla','ap','descripcion','paciente']
     widgets = {
      'ap': DateInput(),
      'descripcion': forms.Textarea(attrs={'placeholder': u'Ingrese Texto de la Consulta'}),
       'paciente': forms.HiddenInput()
     }

class ConsultaDetailForm(ModelForm):

    def __init__(self, *args, **kwargs):
       super(ConsultaDetailForm, self).__init__(*args, **kwargs)
       fields = Consulta._meta.get_fields()
    #   pass first two fields included id
       iterfields = iter(fields)
    
    #    next(iterfields)
    #    next(iterfields)
    #    refactoring the above code
       for x in range(2):
           next(iterfields)
           
    #   iterate and change attribute to readonly
       for field in iterfields:     
           if 'created' != field.name and 'modified' != field.name:              
               self.fields[field.name].widget.attrs['readonly'] = True
    
    #    other way to code change with more lines
     
    #    self.fields['dni'].widget.attrs['readonly'] = True
    #    self.fields['nya'].widget.attrs['readonly'] = True
    #    self.fields['telefono'].widget.attrs['readonly'] = True
    #    self.fields['celular'].widget.attrs['readonly'] = True
    #    self.fields['direccion'].widget.attrs['readonly'] = True
    #    self.fields['mail'].widget.attrs['readonly'] = True
    #    self.fields['cp'].widget.attrs['readonly'] = True
    #    self.fields['fecha_nac'].widget.attrs['readonly'] = True
    #    self.fields['peso_nac'].widget.attrs['readonly'] = True
    #    self.fields['ciudad'].widget.attrs['readonly'] = True
    
    class Meta:
        model=Consulta
        fields='__all__'
