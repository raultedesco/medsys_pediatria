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
from .views import ConsultaListView, ConsultaCreation,ConsultaDetail,ConsultaDelete, ConsultaUpdate
app_name='consultas'
urlpatterns = [
   path('<pk>', ConsultaListView.as_view(), name='list'),
   path('create/<pk>', ConsultaCreation.as_view(), name='create' ),
   path('detalle/<int:paciente_id>/consulta/<int:pk>/', ConsultaDetail.as_view(), name='detail' ),
   path('editar/<int:paciente_id>/consulta/<int:pk>', ConsultaUpdate.as_view(),name="editar"),
   path('borrar/<int:paciente_id>/consulta/<int:pk>/', ConsultaDelete.as_view(), name='delete')
]