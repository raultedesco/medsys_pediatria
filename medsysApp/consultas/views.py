from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.utils import timezone
from datetime import datetime as dt
from pacientes.utils import calcular_edad
from .models import Consulta, Paciente
from obrasocial.models import Afiliado
from turnos.models import turno
from .forms import ConsultaForm, ConsultaDetailForm, ConsultaUpdateForm

from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

class ConsultaListView(ListView):
    model = Consulta
    template_name = "consultas/paciente_consultas.html"
    def get_queryset(self):
        print(self.kwargs)
        #self.paciente = get_object_or_404(Paciente, name=self.kwargs['paciente'])
        self.paciente=self.kwargs['pk']
        print(self.paciente)
        consultas = Consulta.objects.filter(paciente_id=self.paciente)
        return consultas
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paciente_id = self.kwargs['pk']
        paciente = get_object_or_404(Paciente, id=paciente_id)
        context['paciente'] = paciente

        if Afiliado.objects.filter(paciente_id=paciente_id).exists():
           instance_afiliado = Afiliado.objects.get(paciente_id=paciente_id)
           context['os']= instance_afiliado.ObraSocial
        else:
           context['os']=  'Sin Obra Social'

                #Pacientes en Espera
        now = timezone.now().date()
        turnos_today = turno.objects.filter(fecha_turno__contains=now)
        context['lista_espera'] = turnos_today
        return context     
        
class ConsultaCreation(CreateView):
    model = Consulta
    success_url = reverse_lazy('pacientes:list')
    # fields ='__all__'
    form_class = ConsultaForm
    
    def get_initial(self, *args, **kwargs):
        initial = super(ConsultaCreation, self).get_initial(**kwargs)
        paciente_id = self.kwargs['pk']
        initial['paciente'] = paciente_id
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paciente_id = self.kwargs['pk']
        paciente = get_object_or_404(Paciente, id=paciente_id)
        context['paciente'] = paciente
        if paciente:
            if paciente.fecha_nac is not None:
                conv = dt.combine(paciente.fecha_nac, dt.min.time())
                context['edad']= calcular_edad(conv)
         
            else:
                context['edad']= 'Sin Edad'



        return context   
    def get_success_url(self):
        return reverse('consultas:list', kwargs={'pk': self.kwargs['pk']})

class ConsultaDetail(DetailView):
    model = Consulta
    template_name = "consultas/consulta_datos.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paciente_id = self.kwargs['paciente_id']
        print(paciente_id)
        paciente = get_object_or_404(Paciente, id=paciente_id)

        if paciente:
            if paciente.fecha_nac is not None:
                print('entre al otro if')
                conv = dt.combine(paciente.fecha_nac, dt.min.time())
                context['edad']= calcular_edad(conv)
        
            else:
                context['edad']= 'Sin Edad'
        return context

class ConsultaUpdate(UpdateView):
    model = Consulta
    # success_url = reverse_lazy('turnos:list')
    # fields = ['peso', 'perimetro_encef','talla','descripcion','fecha_consulta','paciente' ]
    #fields = '__all__'
    template_name_suffix = '_update_form'
    form_class = ConsultaUpdateForm
    def get_success_url(self):
        return reverse('consultas:list', kwargs={'pk': self.kwargs['paciente_id']})

class ConsultaDelete(DeleteView):
    model = Consulta
    success_url = reverse_lazy('pacientes:list')

    def get_success_url(self):
        return reverse('consultas:list', kwargs={'pk': self.kwargs['paciente_id']})
