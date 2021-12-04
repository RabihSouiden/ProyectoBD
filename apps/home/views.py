
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import base64


from apps.home.decorators import allowed_users, admin_only
from apps.home.forms import MascotaForm, eventoForm, publicacionForm
from apps.home.models import MASCOTA
from apps.home.db import *



@login_required(login_url="/login/")
@admin_only
@allowed_users(allowed_roles=[3])
def index_admin(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
@allowed_users(allowed_roles=[1])
def index_propietario(request):
    form = MascotaForm(request.POST or None)
    usuario = request.user.username
    records = consultar(usuario)
    if form.is_valid():
        nombre = form.cleaned_data.get("nombre")
        especie = form.cleaned_data.get("especie")
        edad = form.cleaned_data.get("edad")
        tamano = form.cleaned_data.get("tamano")
        sexo = form.cleaned_data.get("sexo")
        potencial = form.cleaned_data.get("potencialmente_peligroso")
        microchip = form.cleaned_data.get("microchip")
        insertar_mascota(nombre,especie,potencial,microchip,edad,tamano,sexo, usuario)
    context = {'segment': 'index', 'records' : records, "form": form,}
    html_template = loader.get_template('home/index_propietario.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
@allowed_users(allowed_roles=[1])
def social_propietario(request):
    usuario = request.user.username
    form = publicacionForm(request.POST, client=usuario)
    if request.method == 'POST'and request.FILES['upload']:
        upload = request.FILES['upload']
        fss = FileSystemStorage()
        file = fss.save(upload.name, upload)
        file_url = fss.url(file)
        image = open('C:/Users/santi/OneDrive - unbosque.edu.co/Documentos/IX Semestre/BDII/Proyecto Final/ProyectoBDII/core/'+file_url, "rb")
        image_read = image.read()
        image_64_encode = base64.encodebytes(image_read)
        print(form.errors)
        if form.is_valid():
            titulo = form.cleaned_data.get("titulo")
            descripcion = form.cleaned_data.get("descripcion")
            mascota = form.cleaned_data.get("mascotas")
            nueva_publicacion(usuario,mascota,descripcion,titulo,image_64_encode)
            print(titulo+descripcion+mascota)
        # image_64_decode = base64.decodebytes(image_64_encode) 
        # image_result = open('deer_decode.jpg', 'wb') # create a writable image and write the decoding result
        # image_result.write(image_64_decode)
    records = consultar_publicaciones()
    context = {'segment': 'social', 'records' : records, "form": form,}
    html_template = loader.get_template('home/icons.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
@allowed_users(allowed_roles=[2])
def index_veterinaria(request):
    form = eventoForm(request.POST)
    records = consultar_eventos()
    if form.is_valid():
        tipo_evento = form.cleaned_data.get("tipo_evento")
        descripcion = form.cleaned_data.get("descripcion")
        mascotas = form.cleaned_data.get("mascotas")
        insertar_evento(tipo_evento,descripcion,mascotas)
    context = {'segment': 'index', 'records': records, 'form': form}

    html_template = loader.get_template('home/index_veterinaria.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))

