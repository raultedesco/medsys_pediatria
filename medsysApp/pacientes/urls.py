"""medsys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from .views import (PacienteCreate, 
                    PacienteListView,
                    PacienteDetail,
                    PacienteUpdate,
                    PacienteBrief,
                    PacienteDelete,
                    getConsultas,
                    getDataChart)

app_name='pacientes'
urlpatterns = [
  #path('', home_pacientes, name='home_pacientes'),
  #path('datos/', paciente_datos, name='paciente_datos'),
  path('', PacienteListView.as_view(), name='list'),
  path('nuevo/paciente/',PacienteCreate.as_view(), name='create'),
  path('brief/paciente/<int:pk>', PacienteBrief.as_view(), name='brief'),
  path('detalle/paciente/<int:pk>/', PacienteDetail.as_view(), name='detail' ),
  path('editar/paciente/<int:pk>/', PacienteUpdate.as_view(), name='edit'),
  path('borrar/paciente/<int:pk>/', PacienteDelete.as_view(), name='delete'),
  path('get_consultas/<pk>/', getConsultas, name='consults'),
  path('api/data/<pk>',getDataChart, name='api-data' )
]