from django.core import serializers
from django.shortcuts import render , HttpResponse, get_object_or_404
import json
from django.utils import timezone
from datetime import datetime as dt
from datetime import time 
from django.urls import reverse, reverse_lazy 
from django.http import JsonResponse
from .models import turno, Paciente
from .forms import TurnoForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import(
    CreateView,
    UpdateView,
    DeleteView
)

# Create your views here.


class TurnoListView(ListView):
    model = turno
    template_name = 'turnos/turnos_list.html'
    ordering = ['-created']
    def get_queryset(self):
        # now = dt.now().date()
        # today = dt.combine(now, time())
        now = timezone.now().date()
        # today = dt.combine(now, time())
        # print(now,'today:',today)
        turnos_today = turno.objects.filter(fecha_turno__contains=now)
        for e in turnos_today:
            print(e.fecha_turno)
        return turnos_today

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pacientes_id = self.kwargs['pk']
        now = timezone.now().date()
        turnos_today = turno.objects.filter(fecha_turno__contains=now)
        # instance_turnos = turno.objects.all()
        context['lista_espera'] = turnos_today
        return context

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     turnos_history = turno.objects.all()
    #     context['turnos_history'] = turnos_history
    #     return context    

class TurnosHistoryListView(ListView):
    model = turno
    template_name = 'turnos/turnos__history_list.html'
    ordering = ['-created']

class TurnoCreation(CreateView):
    model = turno
    success_url = reverse_lazy('turnos:list')
    # fields ='__all__'
    form_class = TurnoForm

    # def get_initial(self, *args, **kwargs):
    #     initial = super(TurnoCreation, self).get_initial(**kwargs)
    #     paciente_id = self.kwargs['pk']
    #     initial['paciente_id'] = paciente_id
    #     return initial

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     paciente_id = self.kwargs['pk']
    #     paciente = get_object_or_404(Paciente, id=paciente_id)
    #     context['paciente'] = paciente
    #     return context

    # def get_success_url(self):
    #     return reverse('turnos:list', kwargs={'pk': self.kwargs['pk']})

class TurnoDetail(DetailView):
    model = turno
    template_name = "turnos/turnos.html"

class TurnoDetail(DetailView):
    model = turno
    
    template_name = "turnos/turno_detail.html"
    fields = '__all__'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     afiliado_id = self.kwargs['pk']
    #     instance_afiliado = get_object_or_404(Afiliado, pk=afiliado_id)
    #     context['form'] = AfiliadoDetailForm(instance=instance_afiliado)
    #     return context

class TurnoUpdate(UpdateView):
    model = turno
    success_url = reverse_lazy('turnos:list')
    fields = ['fecha_turno', 'nya','paciente_id','tratado' ]
    #fields = '__all__'
    template_name_suffix = '_update_form'

    # def get_success_url(self):
    #     # if 'slug' in self.kwargs:
    #     #     slug = self.kwargs['slug']
    #     # else:
    #     #     slug = 'demo'
    #     print('pk in get success url:',self.object.id)
    #     return reverse('turnos:list', kwargs={'pk': self.object.id})

class TurnoDelete(DeleteView):
    model = turno
    success_url = reverse_lazy('turnos:list')
