from django.db import models
from pacientes.models import Paciente

# Create your models here.
class Consulta(models.Model):
    peso = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    perimetro_encef = models.CharField(max_length=45, blank=True, null=True)
    talla = models.DecimalField(decimal_places=2, max_digits=8, blank=True, null=True)
    descripcion = models.CharField(max_length=999, blank=True, null=True)
    fecha_consulta = models.DateField(auto_now_add=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    ap= models.DateField(blank=True, null=True)

