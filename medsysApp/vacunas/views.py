from django.core import serializers
from django.shortcuts import render , HttpResponse, get_object_or_404
import json
from django.urls import reverse, reverse_lazy 
from django.http import JsonResponse
from .models import vacuna, vacuna_periodo, vacuna_tipo, Paciente
from .forms import VacunaForm
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import(
    CreateView,
    UpdateView,
    DeleteView
)

#ABM Vacunas


class VacunaListView(ListView):
    model = vacuna
    template_name = 'vacunas/vacunas_list.html'

    def get_queryset(self):
        print(self.kwargs)
        #self.paciente = get_object_or_404(Paciente, name=self.kwargs['paciente'])
        self.paciente=self.kwargs['pk']
        print(self.paciente)
        vacunas = vacuna.objects.filter(paciente_id=self.paciente)
        return vacunas
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paciente_id = self.kwargs['pk']
        print(paciente_id)
        paciente = get_object_or_404(Paciente, id=paciente_id)
        context['paciente'] = paciente
        return context    





class VacunaCreation(CreateView):
    model = vacuna
    # success_url = reverse_lazy('vacunas:list')
    # fields ='__all__'
    form_class = VacunaForm

    def get_initial(self, *args, **kwargs):
        initial = super(VacunaCreation, self).get_initial(**kwargs)
        paciente_id = self.kwargs['pk']
        initial['paciente_id'] = paciente_id
        return initial

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paciente_id = self.kwargs['pk']
        paciente = get_object_or_404(Paciente, id=paciente_id)
        context['paciente'] = paciente
        return context

    def get_success_url(self):
        return reverse('vacunas:list', kwargs={'pk': self.kwargs['pk']})

# class VacunaDetail(DetailView):
#     model = vacuna
#     template_name = "vacunas/vacunas.html"

class VacunaDetail(DetailView):
    model = vacuna
    
    template_name = "vacunas/vacuna_detail.html"
    fields = '__all__'
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     afiliado_id = self.kwargs['pk']
    #     instance_afiliado = get_object_or_404(Afiliado, pk=afiliado_id)
    #     context['form'] = AfiliadoDetailForm(instance=instance_afiliado)
    #     return context

class VacunaUpdate(UpdateView):
    model = vacuna
    #success_url = reverse_lazy('pacientes:list')
    fields = ['fecha_aplicacion','periodo_id','tipo_id','paciente_id' ]
    #fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse('vacunas:list', kwargs={'pk': self.kwargs['paciente_id']})

class VacunaDelete(DeleteView):
    model = vacuna

    
    def get_success_url(self):
        return reverse('vacunas:list', kwargs={'pk': self.kwargs['paciente_id']})









###otros metodos probados



# Create your views here.
# def home_vacunas(request):
#     periodo = vacuna_periodo.objects.all()
#     tipo =  vacuna_tipo.objects.all()
#     vacunas = vacuna.objects.all().order_by('periodo_id')
#     context={'periodo': periodo, 'tipo':tipo, 'vacuna':vacunas}
    
#     return render(request, 'vacunas/paciente_vacunas.html', context)

def vacunas_pac(request,pk=None, *args, **kwargs):
    tipo =  vacuna_tipo.objects.all()
    vacunas = vacuna.objects.all().filter(paciente_id=pk)
    context={'tipo':tipo,'vacuna':vacunas}
    
    return render(request, 'vacunas/paciente_vacunas.html', context)


def getVacunas(request, pk=None, *args, **kwargs):
    print("llego el valor de pk:", pk)

    if request.method == "GET" and request.is_ajax():
 
        print("llego el valor de pk:", pk)

        try:

            v1 = vacuna.objects.filter(periodo_id=pk)
            print(v1)
        
        except:
            return JsonResponse({"success": False}, status=400)

        #return JsonResponse(serializers.serialize('json', v1), status=200, safe=False)
        return HttpResponse(serializers.serialize('json', v1), content_type="application/json")
    return JsonResponse({"success": False}, status=400)


