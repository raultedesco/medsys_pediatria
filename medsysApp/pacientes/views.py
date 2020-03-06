from django.shortcuts import render, get_object_or_404, HttpResponse
from django.db.models import Count
import json
from .utils import calcular_edad
from datetime import datetime as dt
from django.http import JsonResponse
from django.urls import reverse_lazy, reverse
from django.views.generic import ListView
from django.utils import timezone
from django.forms.models import model_to_dict
from .models import Paciente, Provincia
from obrasocial.models import Afiliado
from consultas.models import Consulta
from vacunas.models import vacuna
from turnos.models import turno
from .forms import PacientesForm, PacienteDetailForm
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView,
)
# Create your views here.
# def home_pacientes(request):
#     query_set = Paciente.objects.all()
#     context ={'query_result':query_set}

#     return render(request,'pacientes/pacientes_list.html',context)

# def paciente_datos(request):
#     return render(request, 'pacientes/paciente_datos.html')

def calculate_age(born):
    today = dt.today()
    age = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
    
    return age




class PacienteCreate(CreateView):
    model = Paciente
    # fields = '__all__'
    success_url = reverse_lazy('pacientes:list')
    form_class = PacientesForm


class PacienteListView(ListView):
    model = Paciente
    template_name = "pacientes/pacientes_list.html"

    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # pacientes_id = self.kwargs['pk']
        now = timezone.now().date()
        turnos_today = turno.objects.filter(fecha_turno__contains=now)
        # instance_turnos = turno.objects.all()
        q = Paciente.objects.all()
        pacientes_tmp=[]
        afiliados_tmp=[]
        for e in q:
            
            m = model_to_dict(e)
            if m['fecha_nac'] is not None:
                conv = dt.combine(m['fecha_nac'], dt.min.time())
                m['edad']= calcular_edad(conv)
         
            else:
                m['edad']= 'Sin Edad'

            pacientes_id = e.id
            if Afiliado.objects.filter(paciente_id=pacientes_id).exists():
                instance_afiliado = Afiliado.objects.get(paciente_id=pacientes_id)
                afiliados_tmp.append(instance_afiliado.ObraSocial)
                m['os']= instance_afiliado.ObraSocial
            else:
                afiliados_tmp.append('Sin Obra Social')
                m['os']= 'Sin Obra Social'


            
            pacientes_tmp.append(m)
                
        
        # print(calcular_edad(dt.strptime('2012-10-25 13:18:42.694816','%Y-%m-%d %H:%M:%S.%f')))
        # print(calculate_age(dt.strptime('2019-02-01 13:18:42.694816','%Y-%m-%d %H:%M:%S.%f')))
        # print('tipo despues de la conversion', type(dt.strptime('2012-10-25 13:18:42.694816','%Y-%m-%d %H:%M:%S.%f')))
        context['lista_espera'] = turnos_today
        context['pacientes_f'] = pacientes_tmp
        print(context['pacientes_f'])
        context['afiliado'] = afiliados_tmp
        return context


class PacienteDetail(DetailView):
    model = Paciente

    template_name = "pacientes/paciente_datos.html"
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pacientes_id = self.kwargs['pk']
        instance_paciente = get_object_or_404(Paciente, pk=pacientes_id)
        context['form'] = PacienteDetailForm(instance=instance_paciente)
        if instance_paciente:
            if instance_paciente.fecha_nac is not None:
                conv = dt.combine(instance_paciente.fecha_nac, dt.min.time())
                context['edad']= calcular_edad(conv)
         
            else:
                context['edad']= 'Sin Edad'
            
        return context


class PacienteUpdate(UpdateView):
    model = Paciente
    template_name_suffix = '_update_form'
    form_class = PacientesForm

    def get_success_url(self):
        return reverse('pacientes:detail', kwargs={'pk': self.object.id})



class PacienteBrief(DeleteView):
    model = Paciente
    template_name = 'pacientes/paciente_brief.html'
    fields = '__all__'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        pacientes_id = self.kwargs['pk']

        if Afiliado.objects.filter(paciente_id=pacientes_id).exists():
            instance_afiliado = Afiliado.objects.get(paciente_id=pacientes_id)
            context['afiliado'] = instance_afiliado
        else:
            context['afiliado'] = 'Sin Obra Social'
        consultas_list = Consulta.objects.filter(paciente_id=pacientes_id)
        context['consultas_list'] = consultas_list
        context['consultas_count'] = consultas_list.count()

        #cantidad de Vacunas
        vacunas_list = vacuna.objects.filter(paciente_id=pacientes_id)
        context['vacunas_list'] = vacunas_list
        context['vacunas_count'] = vacunas_list.count()
        #Pacientes en Espera
        now = timezone.now().date()
        turnos_today = turno.objects.filter(fecha_turno__contains=now)
        context['lista_espera'] = turnos_today
        return context


class PacienteDelete(DeleteView):
    model = Paciente
    success_url = reverse_lazy('pacientes:list')


def getConsultas(request, pk=None, *args, **kwargs):

    if request.method == "GET" and request.is_ajax():
        pacientes_id = pk
        print("llego el valor de pk:", pk)

        try:

            afiliado = Afiliado.objects.get(paciente_id=pacientes_id)
            #   print(afiliado.values.nya)
        
        except:
            return JsonResponse({"success": False}, status=400)
        afiliado_info = {
            "nya": afiliado.nya,
            "n_afiliado": afiliado.n_afiliado,
            "obrasocial": afiliado.ObraSocial.ObraSocial,
        }
        return JsonResponse({"consulta_info": afiliado_info}, status=200)
    return JsonResponse({"success": False}, status=400)


def getDataChart(request, pk=None, *args, **kwargs):

    if request.method == "GET" and request.is_ajax():
        pacientes_id = pk
        print("llego el valor de pk en getdatachart:", pk)


        try:

            Consultas_by_paciente = Consulta.objects.filter(paciente_id=pacientes_id)

            default_data = []
            labels=[]
            labelsTalla=[]
            default_dataTalla =[]
            for item in Consultas_by_paciente:
  
                if item.peso is not None:
                    default_data.append(item.peso)
                    labels.append(item.fecha_consulta)

                if item.talla is not None:
                    default_dataTalla.append(item.talla)
                    labelsTalla.append(item.fecha_consulta)
            data = {'labels':labels, 
                    'default_data':default_data,
                    'labelsTalla':labelsTalla,
                    'default_dataTalla':default_dataTalla}
            print(data)
        except:
   
            return JsonResponse({"success": False}, status=400)
 
        return JsonResponse(data, status=200)


    return JsonResponse({"success": False}, status=400)




     