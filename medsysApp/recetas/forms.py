from django import forms
from django.forms import ModelForm
from .models import Receta, RecetaHeader, RecetaFooter, RecetaSnippet, RecetaTemplate

class RecetaPrintForm(forms.Form):
    
    descripcion = forms.CharField(widget=forms.Textarea)

class DateInput(forms.DateInput):
    input_type = 'date'


class RecetaForm(ModelForm):

    class Meta:
     model = Receta
     fields = ['descripcion','paciente_id','template_id']
    #  fields = '__all__'
    #  fields = ['peso', 'perimetro_encef','talla','descripcion','fecha_consulta','paciente']
     widgets = {
       'descripcion': forms.Textarea(attrs={'placeholder': u'Ingrese Texto de la Receta', 'class':'form-control'}),
       'paciente_id': forms.HiddenInput()
       
     }


class RecetaHeaderForm(ModelForm):
    class Meta:
        model = RecetaHeader
        fields = ['header', 'logo','orientacion']
        widgets  = {
            'header': forms.Textarea(attrs={'class':'form-control'}),

        }

class RecetaHeaderUpdateForm(ModelForm):
    logo = forms.ImageField(label='Logo',required=False, error_messages = {'invalid':"Image files only"}, widget=forms.FileInput)
    class Meta:
        model = RecetaHeader
        fields = ['header', 'logo','orientacion']
        widgets  = {
            'header': forms.Textarea(attrs={'class':'form-control'}),
            'orientacion':forms.Select(attrs={'class': 'form-control'})

        }

class RecetaFooterForm(ModelForm):
    class Meta:
        model = RecetaFooter
        fields = ['footer' ,'orientacion']
        widgets  = {
            # 'footer': forms.Textarea(attrs={'placeholder': u'Ingrese Texto del Pie de Pagina'}),
            'footer': forms.Textarea(attrs={'class':'form-control'}),

        }

class RecetaFooterUpdateForm(ModelForm):
    class Meta:
        model = RecetaFooter
        fields = ['footer' ,'orientacion']
        widgets  = {
            # 'footer': forms.Textarea(attrs={'placeholder': u'Ingrese Texto del Pie de Pagina'}),
            'footer': forms.Textarea(attrs={'class':'form-control'}),
            'orientacion':forms.Select(attrs={'class': 'form-control'})


        }

class RecetaSnippetForm(ModelForm):
    class Meta:
        model = RecetaSnippet
        fields = ['snippet' ]
        widgets  = {
            # 'footer': forms.Textarea(attrs={'placeholder': u'Ingrese Texto del Pie de Pagina'}),
            'snippet': forms.Textarea(attrs={'class':'form-control'}),

        }


class RecetaTemplateForm(ModelForm):
    # OrientacionChoices = forms.ChoiceField(choices=RecetaTemplate.OR_CHOICES)
    class Meta:
        model = RecetaTemplate
        fields = ['name','header_id','footer_id','default_template','orientacion']
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control'}),
                 }

class RecetaTemplateUpdateForm(ModelForm):
    # OrientacionChoices = forms.ChoiceField(choices=RecetaTemplate.OR_CHOICES)
    class Meta:
        model = RecetaTemplate
        fields = ['name','header_id','footer_id','default_template','orientacion']
        widgets ={
            'name': forms.TextInput(attrs={'class':'form-control'}),
            'orientacion':forms.Select(attrs={'class': 'form-control'})
                 }