from django.contrib import admin
from .models import Provincia, Ciudad, Paciente
# Register your models here.
admin.site.register(Provincia)
admin.site.register(Ciudad)
admin.site.register(Paciente)