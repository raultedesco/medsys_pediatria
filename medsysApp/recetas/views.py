import io
from django.conf import settings
from django.http import FileResponse
from django.shortcuts import HttpResponse, get_object_or_404, render, HttpResponseRedirect, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import (CreateView, DeleteView, FormView, UpdateView)
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle, TA_CENTER, TA_LEFT
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph, SimpleDocTemplate, Table, TableStyle, Image

from .forms import RecetaForm, RecetaPrintForm, RecetaHeaderForm, RecetaFooter, RecetaSnippet, RecetaTemplate, RecetaFooterForm, RecetaFooterUpdateForm, RecetaHeaderUpdateForm, RecetaTemplateForm, RecetaSnippetForm, RecetaTemplateUpdateForm
from .models import Paciente, Receta, RecetaHeader, RecetaFooter, RecetaSnippet,RecetaTemplate
from obrasocial.models import Afiliado
from .pdf_utils import *
import os
from django.conf import settings

# Create your views here.

def get_styles_customs(tipo):
    styles = getSampleStyleSheet() 
    print(tipo)
    if tipo == 'Titulo_Center':
        print('ingrese al primer if')
        Style_heading1_Center = ParagraphStyle('titulo1_centrado', 
                           alignment = TA_CENTER,
                        #    fontSize = 10,
                        #    fontName="Helvetica",
                           parent=styles['Heading1'],)
        return Style_heading1_Center

    if tipo == 'Titulo2_Center':
        print('ingrese al primer if')
        Style_heading2_Center = ParagraphStyle('titulo2_centrado', 
                           alignment = TA_CENTER,
                        #    fontSize = 10,
                        #    fontName="Helvetica",
                           parent=styles['Heading2'],)
        return Style_heading2_Center

    if tipo == 'Normal_Center':
        Style_normal_Center = ParagraphStyle('titulo1_centrado', 
                            alignment = TA_CENTER,
                            fontSize = 14,
                            leading = 28,
                            spacebefore=60,
                            spaceAfter=14,
                            
                        #    fontName="Helvetica",
                           parent=styles['Normal'],)
    
        return Style_normal_Center
    if tipo == 'Normal_Left':
        Style_normal_Left = ParagraphStyle('titulo1_centrado', 
                           alignment = TA_LEFT,
                            fontSize = 14,
                            leading = 28,
                            spacebefore=40,
                            spaceAfter=14,
                        #    fontName="Helvetica",
                           parent=styles['Normal'],)
    
        return Style_normal_Left
    if tipo == 'Footer_Center':
        Style_footer_Center = ParagraphStyle('parrafos', 
                           alignment = TA_CENTER,
                           fontSize = 10,
                           fontName="Helvetica")
        return Style_footer_Center
    else:
        Style_selected = styles['Normal']
    return Style_selected

class RecetaListView(ListView):
    model = Receta
    template_name = 'recetas/recetas_list.html'

    def get_queryset(self):
        print(self.kwargs)
        #self.paciente = get_object_or_404(Paciente, name=self.kwargs['paciente'])
        self.paciente=self.kwargs['pk']
        print(self.paciente)
        consultas = Receta.objects.filter(paciente_id=self.paciente)
        return consultas
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paciente_id = self.kwargs['pk']
        paciente = get_object_or_404(Paciente, id=paciente_id)
        context['paciente'] = paciente
        return context    

class RecetaCreation(CreateView):
    model = Receta
    success_url = reverse_lazy('pacientes:list')
    form_class = RecetaForm

    def get_initial(self, *args, **kwargs):
        initial = super(RecetaCreation, self).get_initial(**kwargs)
        paciente_id = self.kwargs['pk']
        initial['paciente_id'] = paciente_id
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paciente_id = self.kwargs['pk']
        snippets = RecetaSnippet.objects.all()
        paciente = get_object_or_404(Paciente, id=paciente_id)
        afiliado = get_object_or_404(Afiliado, paciente_id=paciente_id)
        context['paciente'] = paciente
        context['afiliado'] = afiliado
        context['snippets'] = snippets
        return context   
    
    def form_valid(self, form, *args, **kwargs):
        self.object = form.save()
        paciente_id = self.kwargs['pk']
        print('algo despues de guardar la receta')
        t_id = self.request.POST.get('template_id')
        print(t_id)
        # return receta_print(self.request, paciente_id)
        template = get_object_or_404(RecetaTemplate, id=t_id)
        return gen_pdf(self.request, template)
        # do something with self.object
        # remember the import: from django.http import HttpResponseRedirect
        #return HttpResponseRedirect(self.get_success_url())

def preview_template(request, pk):
    print('recibi el id de template:', pk)
    template = get_object_or_404(RecetaTemplate, id = pk)
    return preview_template_asPDF(request,template)

def getDefaultTemplate(request):
    template = RecetaTemplate.objects.filter(default_template=True)[0]
    print(template.default_template)
    return preview_template_asPDF(request, template)

def view_receta(request, pk):
    receta = get_object_or_404(Receta, id=pk)
    return view_receta_stored(request,receta)

def get_receta_paciente_afiliado(pk):
    receta = get_object_or_404(Receta, id=pk)
    # print(receta.descripcion)
    paciente_id =receta.paciente_id.id
    paciente = get_object_or_404(Paciente, id=paciente_id)
    # print(paciente)
    # afiliado = get_object_or_404(Afiliado, id=paciente_id)
    try:
        afiliado = Afiliado.objects.get(id=paciente_id)
    except Afiliado.DoesNotExist:
        afiliado = 'Sin Obra Social'
        print(afiliado)
    return receta, paciente, afiliado

def RecetasCustom(request):
    return render(request,'recetas/recetas_templates.html')

class RecetaHeaderListView(ListView):
    model = RecetaHeader
    template_name = 'recetas/recetas_header_list.html'

class RecetaFooterListView(ListView):
    model = RecetaFooter
    template_name = 'recetas/recetas_footer_list.html'

class RecetaSnippetListView(ListView):
    model = RecetaSnippet
    template_name = 'recetas/recetas_snippet_list.html'

class CreationHeaderCustomView(CreateView):
    model = RecetaHeader
    success_url = reverse_lazy('recetas:header_list')
    template_name = 'recetas/header_form.html'
    form_class = RecetaHeaderForm
    # return render(request, 'recetas/edit_header.html')

class CreationFooterCustomView(CreateView):
    model = RecetaFooter
    success_url = reverse_lazy('recetas:footer_list')
    template_name = 'recetas/footer_form.html'
    # fields = ['footer']
    form_class = RecetaFooterForm

class CreationSnippetCustomView(CreateView):
    model = RecetaSnippet
    success_url = reverse_lazy('recetas:snippet_list')
    template_name = 'recetas/snippet_form.html'
    # fields = ['footer']
    form_class = RecetaSnippetForm

class HeaderUpdateView(UpdateView):
    model = RecetaHeader
    template_name = 'recetas/header_update_form.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('recetas:header_list')
    form_class = RecetaHeaderUpdateForm

class FooterUpdateView(UpdateView):
    model = RecetaFooter
    template_name = 'recetas/footer_update_form.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('recetas:footer_list')
    form_class = RecetaFooterUpdateForm

class SnippetUpdateView(UpdateView):
    model = RecetaSnippet
    template_name = 'recetas/snippet_update_form.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('recetas:snippet_list')
    form_class = RecetaSnippetForm   

class TemplateUpdateView(UpdateView):
    model = RecetaTemplate
    template_name = 'recetas/template_update_form.html'
    template_name_suffix = '_update_form'
    success_url = reverse_lazy('recetas:template_list')
    form_class = RecetaTemplateUpdateForm

class HeaderDelete(DeleteView):
    model = RecetaHeader
    success_url = reverse_lazy('recetas:header_list')
class FooterDelete(DeleteView):
    model = RecetaFooter
    success_url = reverse_lazy('recetas:footer_list')
class SnippetDelete(DeleteView):
    model = RecetaSnippet
    success_url = reverse_lazy('recetas:snippet_list')
class TemplateDelete(DeleteView):
    model = RecetaTemplate
    success_url = reverse_lazy('recetas:template_list')

def MakeTemplate(request):
    qheaders = RecetaHeader.objects.all()
    qfooters = RecetaFooter.objects.all() 
    context = {}
    context['headers']=qheaders
    context['footers']=qfooters

    if request.method == 'POST':
        print('ingrese al post')
        print(request.POST)
        form = RecetaTemplateForm(request.POST)

        if form.is_valid():
            #  template_selected = form.cleaned_data['value']
            form.save()
            return redirect('recetas:custom')

    else:
        form = RecetaTemplateForm()
        context['form']=form
    
    return render(request,'recetas/make_template.html', context) 

class RecetaTemplateListView(ListView):
    model = RecetaTemplate
    template_name = 'recetas/recetas_template_list.html'



