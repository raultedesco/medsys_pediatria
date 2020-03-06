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
from .views import (
    VacunaListView,
    VacunaDetail, 
    VacunaCreation,
    VacunaUpdate, 
    VacunaDelete)

app_name='vacunas'

urlpatterns = [
#    path('', views.home_vacunas, name='list'),
   path('<pk>', VacunaListView.as_view(), name='list'),
#    path('get_vacunas/<pk>/', views.getVacunas, name='vacunas'),
   path('create/<pk>', VacunaCreation.as_view(), name='create' ),
   path('detalle/vacuna/<int:pk>/', VacunaDetail.as_view(), name='detail' ),
   path('editar/<int:paciente_id>/vacuna/<int:pk>', VacunaUpdate.as_view(),name="editar"),
   path('borrar/<int:paciente_id>/vacuna/<int:pk>/', VacunaDelete.as_view(), name='delete')
   
]