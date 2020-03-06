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
from .views import ObraSocialDetail,AfiliadoUpdate, AfiliadoDelete, AfiliadoCreate

app_name='obrasocial'
urlpatterns = [
   #path('', views.home_obrasocial, name='home_obrasocial'),
   path('create/afiliado/',AfiliadoCreate.as_view(), name='create' ),
   path('afiliado/<pk>/', ObraSocialDetail.as_view(), name='afiliado' ),
   path('editar/afiliado/<int:pk>', AfiliadoUpdate.as_view(),name="editar"),
   path('borrar/afiliado/<int:pk>', AfiliadoDelete.as_view(), name='delete')
   
]