from django.db import models
from pacientes.models import Paciente
# Create your models here.
class vacuna_periodo(models.Model):
    desc = models.CharField(max_length=100)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)


    def __str__(self):
        return self.desc
    

class vacuna_tipo(models.Model):
    desc = models.CharField(max_length=100)

    def __str__(self):
        return self.desc


class vacuna(models.Model):
    fecha_aplicacion = models.DateField()
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    periodo_id=models.ForeignKey(vacuna_periodo, on_delete=models.CASCADE)
    tipo_id=models.ForeignKey(vacuna_tipo, on_delete=models.CASCADE)
    #paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    paciente_id = models.ForeignKey(Paciente, on_delete=models.CASCADE)
    def __str__(self):
        return str(self.fecha_aplicacion) + ' | '+ str(self.periodo_id) + '-' + str(self.tipo_id) + ' | ' +str(self.paciente_id) 