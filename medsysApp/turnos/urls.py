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
    TurnoListView,
    TurnosHistoryListView,
    TurnoCreation,
    TurnoDetail,
    TurnoDelete,
    TurnoUpdate
    )
app_name='turnos'
urlpatterns = [
   path('', TurnoListView.as_view(), name='list'),
   path('history/turno/', TurnosHistoryListView.as_view(), name='list_history'),
   path('create/', TurnoCreation.as_view(), name='create' ),
   path('detalle/turno/<int:pk>/', TurnoDetail.as_view(), name='detail' ),
   path('editar/turno/<int:pk>', TurnoUpdate.as_view(),name="editar"),
   path('borrar/turno/<int:pk>/', TurnoDelete.as_view(), name='delete')
]