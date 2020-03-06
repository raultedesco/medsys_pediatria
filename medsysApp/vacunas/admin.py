from django.contrib import admin
from .models import vacuna_periodo,vacuna_tipo,vacuna

# Register your models here.
admin.site.register(vacuna_periodo)
admin.site.register(vacuna_tipo)
admin.site.register(vacuna)