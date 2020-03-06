from django.shortcuts import render, redirect
from django.contrib.auth.forms import SetPasswordForm, UserCreationForm
from django.contrib.auth import login, authenticate
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms
from .forms import RegisterForm
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    return render(request, 'registration/register.html')


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/register.html'

    def get_success_url(self):
        return reverse_lazy('login') + '?register'  

    def get_form(self, form_class=None):
        form = super(RegisterView, self).get_form()
        # Modificar en tiempo real
        form.fields['username'].widget = forms.TextInput(
            attrs={'class':'form-control form-control-user', 'placeholder':'Nombre de usuario'})
        form.fields['password1'].widget = forms.PasswordInput(
            attrs={'class':'form-control form-control-user', 'placeholder':'Contraseña'})
        form.fields['password2'].widget = forms.PasswordInput(
            attrs={'class':'form-control form-control-user', 'placeholder':'Repite la contraseña'})
        print(form)
        return form 


class RegisterViewOld(CreateView):
    form_class = RegisterForm
    template_name = 'registration/register.html'
    def form_valid(self, form):
        '''
        En este parte, si el formulario es valido guardamos lo que se obtiene de él y usamos authenticate para que el usuario incie sesión luego de haberse registrado y lo redirigimos al index
        '''
        form.save()
        usuario = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        usuario = authenticate(username=usuario, password=password)
        login(self.request, usuario)
        return redirect('login')



# def set_password(request):
   
#     if request.method  == 'POST':
#         username = request.POST.get('username')
#         if username is not '':
#             print(username)
#             u = User.objects.get(username=username)
#             pform = SetPasswordForm(user=u, data=request.POST)
#             print(pform)
#             if pform.is_valid():
#                 print('form valido')
#                 pform.save()
#                 return HttpResponse('Password Updated')

#     return render(request, 'registration/reset_password.html',{})
#     HttpResponse('No se pudo Actualizar Password')