from django.shortcuts import render, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.utils import timezone
from .models import Afiliado
from .forms import AfiliadoForm, AfiliadoDetailForm

from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

# # Create your views here.
# def home_obrasocial(request):
#     return render(request,'obrasocial/obra_social.html')
class AfiliadoCreate(CreateView):
    model = Afiliado
    # fields = '__all__'
    success_url = reverse_lazy('pacientes:list')
    form_class = AfiliadoForm

    def get_initial(self, *args, **kwargs):
        initial = super(AfiliadoCreate, self).get_initial(**kwargs)
        paciente_id = self.kwargs['pk']
        initial['paciente_id'] = paciente_id
        return initial

class ObraSocialDetail(DetailView):
    model = Afiliado
    template_name = "obrasocial/obra_social.html"

class AfiliadoDetail(DetailView):
    model = Afiliado
    
    template_name = "pacientes/paciente_datos.html"
    fields = '__all__'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        afiliado_id = self.kwargs['pk']
        instance_afiliado = get_object_or_404(Afiliado, pk=afiliado_id)
        context['form'] = AfiliadoDetailForm(instance=instance_afiliado)
        return context

class AfiliadoUpdate(UpdateView):
    model = Afiliado
    #success_url = reverse_lazy('pacientes:list')
    fields = ['nya','n_afiliado','ObraSocial','paciente_id' ]
    #fields = '__all__'
    template_name_suffix = '_update_form'

    def get_success_url(self):
        # if 'slug' in self.kwargs:
        #     slug = self.kwargs['slug']
        # else:
        #     slug = 'demo'
        print('pk in get success url:',self.object.id)
        return reverse('obrasocial:afiliado', kwargs={'pk': self.object.id})

class AfiliadoDelete(DeleteView):
    model = Afiliado
    success_url = reverse_lazy('pacientes:list')