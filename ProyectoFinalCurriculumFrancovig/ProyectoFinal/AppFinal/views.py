from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.template import loader
from AppFinal.models import ExProf, Formacion, Skills, Avatar
from AppFinal.forms import FormularioExProf, FormularioFormacion, FormularioSkills, UserRegisterForm, UserEditForm
from django.db.models import Q
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.urls import reverse_lazy


# Vistas

def inicio(request):
    return render(request, "AppFinal/inicio.html")

def experiencia(request):
    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            experiencias = ExProf.objects.filter( Q(empresa_icontains=search) )
            return render(request, "AppFinal/experienciaprofesional.html", {"experiencias":experiencias, "search":True})
    experiencias = ExProf.objects.all()
    return render(request, "AppFinal/experienciaProfesional.html", {"experiencias":experiencias})

def formacion(request):
    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            formaciones = Formacion.objects.filter( Q(institucion_icontains=search) )
            return render(request, "AppFinal/formacionacademica.html", {"formaciones":formaciones, "search":True})
    formaciones = Formacion.objects.all()
    return render(request, "AppFinal/formacionAcademica.html", {"formaciones":formaciones})

def skill(request):
    if request.method == "POST":
        search = request.POST["search"]
        if search != "":
            skills = Skills.objects.filter( Q(software_icontains=search) )
            return render(request, "AppFinal/skills.html", {"skills":skills, "search":True})
    skills = Skills.objects.all()
    return render(request, "AppFinal/skills.html", {"skills":skills})

def intereses(request):
    return render(request, "AppFinal/intereses.html"  )

# def intereses(self):
#     plantilla = loader.get_template('AppFinal/intereses.html')
#     documento = plantilla.render()
#     return HttpResponse(documento)

#----------------------------------------------------------------
# FORMULARIOS:

def formularioExProf(request):
    if request.method == 'POST':
        miFormulario = FormularioExProf(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            empresa = informacion['empresa']
            puesto = informacion['puesto']
            fechaInicial = informacion['fechaInicial']
            fechaFinal = informacion['fechaFinal']
            descripcion = informacion['descripcion']
            referencia = informacion['referencia']
            telefonoReferencia = informacion['telefonoReferencia']
            experiencia = ExProf(empresa=empresa, puesto=puesto, fechaInicial=fechaInicial, fechaFinal=fechaFinal, descripcion=descripcion, referencia=referencia, telefonoReferencia=telefonoReferencia)
            experiencia.save()
            return render(request, 'AppFinal/inicio.html')
    else:
        miFormulario = FormularioExProf()

    return render(request, 'AppFinal/formularioExProf.html', {"miFormulario":miFormulario})

def formularioFormacion(request):
    if request.method == 'POST':
        miFormulario = FormularioFormacion(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            institucion = informacion['institucion']
            nombreCurso = informacion['nombreCurso']
            fechaInicial = informacion['fechaInicial']
            fechaFinal = informacion['fechaFinal']
            descripcion = informacion['descripcion']
            estado = informacion['estado']
            proyectoFinal = informacion['proyectoFinal']
            formacion = Formacion(institucion=institucion, nombreCurso=nombreCurso, fechaInicial=fechaInicial, fechaFinal=fechaFinal, descripcion=descripcion, estado=estado, proyectoFinal=proyectoFinal)
            formacion.save()
            return render(request, 'AppFinal/inicio.html')
    else:
        miFormulario = FormularioFormacion()

    return render(request, 'AppFinal/formularioFormacion.html', {"miFormulario":miFormulario})

def formularioSkills(request):
    if request.method == 'POST':
        miFormulario = FormularioSkills(request.POST)
        print(miFormulario)

        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            software = informacion['software']
            nivel = informacion['nivel']
            skill = Skills(software=software, nivel=nivel)
            skill.save()
            return render(request, 'AppFinal/inicio.html')
    else:
        miFormulario = FormularioSkills()

    return render(request, 'AppFinal/formularioSkills.html', {"miFormulario":miFormulario})

#----------------------------------------------------------------
# BUSQUEDA DE SKILLS POR NIVEL

# def busquedaSkills(request):
#     return render(request, 'AppFinal/busquedaSkills.html')

# def busqueda(request):
#     if request.GET['nivel']:
#         nivel = request.GET['nivel']
#         skills = Skills.objects.filter(nivel=nivel)
#         return render(request, 'AppFinal/resultadosBusqueda.html', {'skills': skills, 'nivel': nivel})
#     else:
#         respuesta = "No dato ingresado no es válido, intente nuevamente."
#     return HttpResponse(respuesta)

#----------------------------------------------------------------
# CRUD - CBV (Clases basadas en vistas)

# @login_required
class ExProfList(ListView):
    model = ExProf
    template_name = "AppFinal/experiencia_list.html"

class ExProfDetalle(DetailView):
    model = ExProf
    template_name = "AppFinal/exprof_detalle.html"

class ExProfCrear(CreateView):
    model = ExProf
    success_url = reverse_lazy("List")
    fields = ['empresa', 'puesto', 'fechaInicial', 'fechaFinal', 'descripcion', 'referencia', 'telefonoReferencia']

class ExProfUpdate(UpdateView):
    model = ExProf
    success_url = reverse_lazy("List")
    fields = ['empresa', 'puesto', 'fechaInicial', 'fechaFinal', 'descripcion', 'referencia', 'telefonoReferencia']

class ExProfDelete(DeleteView):
    model = ExProf
    success_url = reverse_lazy("List")


class FormacionList(ListView):
    model = Formacion
    template_name = "AppFinal/formacion_list.html"

class FormacionDetalle(DetailView):
    model = Formacion
    template_name = "AppFinal/formacion_detalle.html"

class FormacionCrear(CreateView):
    model = Formacion
    success_url = reverse_lazy("FList")
    fields = ['institucion', 'nombreCurso', 'fechaInicial', 'fechaFinal', 'descripcion', 'estado', 'proyectoFinal']

class FormacionUpdate(UpdateView):
    model = Formacion
    success_url = reverse_lazy("FList")
    fields = ['institucion', 'nombreCurso', 'fechaInicial', 'fechaFinal', 'descripcion', 'estado', 'proyectoFinal']

class FormacionDelete(DeleteView):
    model = Formacion
    success_url = reverse_lazy("FList")


#iniciamos el login
def login_request(request):
      #capturamos el post
      if request.method == "POST":
            #inicio el uso del formulario de autenticación que me da Django
            #me toma dos parámetros el request y los datos que toma del request
            form = AuthenticationForm(request, data = request.POST)
            
            if form.is_valid():
                  usuario = form.cleaned_data.get('username')
                  contra = form.cleaned_data.get('password')
               
                  user = authenticate(username = usuario , password = contra)
                 
                  if user is not None:
                        login(request, user)

                        return render (request, "AppFinal/loginSuccess.html", {"mensaje": f"Bienvenido/a {usuario}"})
                  else:
                       
                        return render (request, "AppFinal/login.html", {"mensaje":"Hubo un error, intentá nuevamente"})
            else:
                  return render(request, "AppFinal/login.html", {"mensaje":"Hubo un error en el formulario"})
      
      #al final recuperamos el form
      form = AuthenticationForm()
    
      return render(request, "AppFinal/login.html", {'form': form})

def register(request):
      
      if request.method == "POST":

            form = UserRegisterForm(request.POST)
            
            if form.is_valid():
                  username = form.cleaned_data['username']
                  form.save()

                  return render(request, "AppFinal/userCreateSuccess.html", {"mensaje": "Usuario creado"})
            
            else:
                 return render(request, "AppFinal/login.html")

      else: 
            form = UserRegisterForm()

      return render(request, "AppFinal/registro.html", {"form": form})

@login_required
def editarPerfil(request):
      #se instancia el Login; 
      usuario = request.user
      
      if request.method == 'POST':
            miFormulario = UserEditForm(request.POST)
            if miFormulario.is_valid(): #si pasa la validación Django
                  informacion = miFormulario.cleaned_data
                  
                  #datos que modificaríamos
                  usuario.email = informacion['email']#alg@algo.com
                  usuario.password1 = informacion['password1']#pass
                  usuario.password2 = informacion['password2']
                  usuario.first_name = informacion['first_name']
                  usuario.last_name = informacion['last_name']
                  usuario.save()
            
                  return render(request, "AppFinal/userEditSuccess.html", {"mensaje": "Usuario modificado"})

      else:
            #creo el formulario con los datos que voy a modificar
            miFormulario = UserEditForm(initial={'email':usuario.email, 'first_name':usuario.first_name, 'last_name':usuario.last_name})
      
      #voy al HTML que me permite editar
      return render(request, "AppFinal/editarPerfil.html", {"miFormulario": miFormulario, "usuario": usuario})


