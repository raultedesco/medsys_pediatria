from django.db import models
#from obrasocial.models import Afiliado
# Create your models here.
class Provincia(models.Model):
    provincia = models.CharField(max_length=50, verbose_name='Provincia')

    def __str__(self):
        return self.provincia


class Ciudad(models.Model):
    ciudad = models.CharField(max_length=50, verbose_name='Ciudad')
    provincia= models.ForeignKey(Provincia, on_delete=models.CASCADE)

    def __str__(self):
        return self.ciudad


class Paciente(models.Model):
    dni = models.IntegerField(blank=True, null=True)
    nya = models.CharField(max_length=200, verbose_name='Nombre y Apellido', blank=True, null=True)
    telefono = models.CharField(max_length=45, blank=True, null=True)
    celular = models.CharField(max_length=45, blank=True, null=True)
    direccion = models.CharField(max_length=200, blank=True, null=True)
    mail = models.CharField(max_length=100, blank=True, null=True)
    cp = models.CharField(max_length=11, blank=True, null=True)
    fecha_nac = models.DateField(default='', blank=True, null=True)
    peso_nac = models.CharField(max_length=50, blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    eg = models.CharField(max_length=50, blank=True, null=True)
    talla = models.CharField(max_length=50, blank=True, null=True)
    pc = models.CharField( max_length=50, blank=True, null=True)
    apgar = models.CharField(max_length=50, blank=True, null=True)
    tutor = models.CharField(max_length=80, blank=True, null=True)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE, verbose_name='Ciudad', default='1')

    def __str__(self):
        return u'%s %s %s' % (self.nya, 'DNI:', self.dni)
          

