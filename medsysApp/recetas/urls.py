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
from .views import (RecetaListView,
 RecetaCreation,
 preview_template,
 view_receta,
 RecetasCustom,
 CreationHeaderCustomView,
 CreationFooterCustomView,
 RecetaFooterListView,
 RecetaHeaderListView,
 RecetaSnippetListView,
 HeaderUpdateView,
 FooterUpdateView,
 SnippetUpdateView,
 MakeTemplate,
 RecetaTemplateListView,
 CreationSnippetCustomView,
 getDefaultTemplate,
 TemplateUpdateView,
 HeaderDelete,
 FooterDelete,
 SnippetDelete,
 TemplateDelete
 
 
#  EditSnippetCustom
)
# from .views import receta_print
app_name='recetas'
urlpatterns = [
  #path('', home_pacientes, name='home_pacientes'),
  #path('datos/', paciente_datos, name='paciente_datos'),
  path('<pk>', RecetaListView.as_view(), name='list'),
  path('custom/', RecetasCustom, name='custom' ),
  path('custom/list/header' ,RecetaHeaderListView.as_view(),name='header_list'),
  path('custom/list/footer' ,RecetaFooterListView.as_view(),name='footer_list'),
  path('custom/list/snippet' ,RecetaSnippetListView.as_view(),name='snippet_list'),
  path('custom/list/templates' ,RecetaTemplateListView.as_view(),name='template_list'),
  path('custom/create/header', CreationHeaderCustomView.as_view(), name='create-custom-header' ),
  path('custom/create/footer', CreationFooterCustomView.as_view(), name='create-custom-footer' ),
  path('custom/create/snippet', CreationSnippetCustomView.as_view(), name='create-custom-snippet' ),
  path('custom/edit/header/<int:pk>', HeaderUpdateView.as_view(), name='edit-custom-header' ),
  path('custom/edit/footer/<int:pk>', FooterUpdateView.as_view(), name='edit-custom-footer' ),
  path('custom/edit/snippet/<int:pk>', SnippetUpdateView.as_view(), name='edit-custom-snippet' ),
  path('custom/edit/template/<int:pk>', TemplateUpdateView.as_view(), name='edit-custom-template' ),
  path('custom/borrar/header/<int:pk>/', HeaderDelete.as_view(), name='delete-header'),
  path('custom/borrar/footer/<int:pk>/', FooterDelete.as_view(), name='delete-footer'),
  path('custom/borrar/snippet/<int:pk>/', SnippetDelete.as_view(), name='delete-snippet'),
  path('custom/borrar/template/<int:pk>/', TemplateDelete.as_view(), name='delete-template'),
   
  path('custom/make/template', MakeTemplate, name='make-template' ),
#   path('custom/edit/footer', EditFooterCustom, name='custom' ),
#   path('custom/edit/snippets', EditSnippetCustom, name='custom' ),
  path('generate/<pk>', RecetaCreation.as_view(), name='add' ),#Se usa en Generate Receta
#   path('print/<pk>', receta_print, name='print'),
  path('api/view_pdf/<pk>', view_receta, name='view_pdf'),#Se uesa en historial de recetas del paciente
  path('api/preview_pdf/<pk>', preview_template, name='preview_pdf'),#Se uesa en historial de recetas del paciente
  path('api/get_default_template', getDefaultTemplate, name='get_default_template' )
]