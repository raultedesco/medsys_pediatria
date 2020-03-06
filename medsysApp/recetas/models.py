from django.db import models
from pacientes.models import Paciente

    
class RecetaFooter(models.Model):
    OR_CHOICES_F = (
        ('I', 'Izquierda'),
        ('C', 'Centrada'),
    )

    footer = models.CharField( max_length=500)
    orientacion = models.CharField(max_length=2 , choices=OR_CHOICES_F)


    def __str__(self):
        return self.footer

class RecetaHeader(models.Model):
    OR_CHOICES_H = (
        ('I', 'Izquierda'),
        ('C', 'Centrada'),
    )

    header = models.CharField(max_length=500)
    logo = models.ImageField(upload_to='header/logo/', max_length=None,blank=True, null=True)
    orientacion = models.CharField(max_length=2 , choices=OR_CHOICES_H)

    def __str__(self):
        return self.header  

class RecetaSnippet(models.Model):
    snippet = models.CharField(max_length=500)

class RecetaTemplate(models.Model):
    OR_CHOICES = (
         ('I', 'Izquierda'),
        ('C', 'Centrada'),
    )

    name = models.CharField(max_length=200)
    header_id = models.ForeignKey(RecetaHeader,on_delete=models.CASCADE)
    footer_id = models.ForeignKey(RecetaFooter , on_delete=models.CASCADE)
    default_template = models.BooleanField(default=False)
    orientacion = models.CharField(max_length=2 , choices=OR_CHOICES)

    def __str__(self):
        return self.name

    def setDefaultTemplate(self, valor):
        self.default_template = valor

    def save(self, *args, **kwargs):
        if self.default_template:
            try:
                temp = RecetaTemplate.objects.get(default_template=True)
                if self != temp:
                    temp.default_template = False
                    temp.save()
            except RecetaTemplate.DoesNotExist:
                pass
        super(RecetaTemplate, self).save(*args, **kwargs)

class Receta(models.Model):
    descripcion = models.CharField(max_length=1000)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    template_id = models.ForeignKey(RecetaTemplate, on_delete=models.CASCADE)