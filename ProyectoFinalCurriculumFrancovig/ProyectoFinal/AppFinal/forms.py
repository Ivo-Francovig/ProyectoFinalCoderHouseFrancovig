from dataclasses import fields
from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class FormularioExProf(forms.Form):
    empresa = forms.CharField(max_length=40)
    puesto = forms.CharField(max_length=40)
    fechaInicial = forms.CharField(max_length=40, label='Fecha inicial')
    fechaFinal = forms.CharField(max_length=40, label='Fecha final')
    descripcion = forms.CharField(max_length=400, label='Descripción')
    referencia = forms.CharField(max_length=40)
    telefonoReferencia = forms.IntegerField()

class FormularioFormacion(forms.Form):
    institucion = forms.CharField(max_length=40, label='Institución')
    nombreCurso = forms.CharField(max_length=50, label='Nombre')
    fechaInicial = forms.CharField(max_length=40, label='Fecha inicial')
    fechaFinal = forms.CharField(max_length=40, label='Fecha final')
    descripcion = forms.CharField(max_length=600, label='Descripción')
    estado = forms.CharField(max_length=40)
    proyectoFinal = forms.CharField(max_length=100, label='Proyecto Final')

class FormularioSkills(forms.Form):
    software = forms.CharField(max_length=40, label='Skill')
    nivel = forms.CharField(max_length=40)

class UserRegisterForm(UserCreationForm):
    username = forms.CharField(label='Usuario')
    email = forms.EmailField(label='E-mail')
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita la contraseña', widget=forms.PasswordInput)
    first_name = forms.CharField(label='nombre')
    last_name = forms.CharField(label='apellido')
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'first_name', 'last_name']
        labels = {'username': 'usuario', 'email':'correo', 'first_name':'nombre','last_name': 'apellido'}
        help_texts= {k:"" for k in fields}

class UserEditForm(UserCreationForm): 
    #definimos lo básico para modificar del usuario
    email = forms.EmailField(label='E-mail')
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    password1 = forms.CharField(label= 'Contraseña', widget= forms.PasswordInput)
    password2 = forms.CharField(label= 'Repita la contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'password1', 'password2']
        labels = {'email':'correo', 'first_name':'nombre','last_name': 'apellido'}
        help_texts= {k:"" for k in fields}