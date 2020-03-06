from django.db import models
from pacientes.models import Paciente
# Create your models here.
class ObraSocial(models.Model):
    ObraSocial = models.CharField(max_length=50)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.ObraSocial

class Afiliado(models.Model):
    nya = models.CharField(max_length=200, verbose_name='Nombre Afiliado', default='Empty', blank=True, null=True)
    n_afiliado = models.CharField(max_length=200, default='Particular')
    ObraSocial = models.ForeignKey(ObraSocial, on_delete=models.CASCADE)
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.nya