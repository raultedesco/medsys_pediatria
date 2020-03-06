from django.db import models
from pacientes.models import Paciente

class turno(models.Model):
    fecha_turno= models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    nya = models.CharField(max_length=100)
    tratado = models.BooleanField(default=False) 
    paciente_id = models.ForeignKey(Paciente, null = True, blank= True, default=0, on_delete=models.CASCADE)
 

