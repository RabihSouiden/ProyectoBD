from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.http import request

from apps.home.db import consultar, consultar_mascotas


class MascotaForm(forms.Form):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre de la Mascota",
                "class": "form-control"
            }
        ))
    especie = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Especie de la Mascota",
                "class": "form-control"
            }
        ))
    SI_NO = [
        ("Si", "Si"),
        ("No", "No"),
        ]
    potencialmente_peligroso = forms.ChoiceField(
            choices=SI_NO,
            initial='0',
            required=True,
            label='pot',
        )
    edad = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Edad de la Mascota",
                "class": "form-control"
            }
        ))
    tamano = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Tamaño de la Mascota",
                "class": "form-control"
            }
        ))
    OPTIONS = [
        ("Macho", "Macho"),
        ("Hembra", "Hembra"),
        ]

    sexo = forms.ChoiceField(
            choices=OPTIONS,
            initial='0',
            required=True,
            label='Sexo',
        )
    microchip = forms.ChoiceField(
            choices=SI_NO,
            initial='0',
            required=True,
            label='microchip',
        )

class publicacionForm(forms.Form):
    def __init__(self,*args,**kwargs):
        myClient = kwargs.pop("client")     # client is the parameter passed from views.py
        super(publicacionForm, self).__init__(*args,**kwargs)
        print(myClient)
        MASCOTAS = []
        records = consultar(myClient)
        for row in records:
            MASCOTAS.append(row[1])
            MASCOTAS.append(row[1])
        self.fields['mascotas'] = forms.ChoiceField(label="mascotas", choices=[MASCOTAS])

    mascotas = forms.ChoiceField()


    titulo = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Titulo",
                "class": "form-control"
            }
        ))
    descripcion = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "descripción",
                "class": "form-control"
            }
        ))
    #imagen = forms.ImageField()

    # MASCOTAS = []
    # usuario = self.usuario
    # records = consultar(usuario)
    # for row in records:
    #     MASCOTAS.append(row[1])
    # mascota = forms.MultipleChoiceField(
    #         choices=MASCOTAS,
    #         initial='0',
    #         widget=forms.SelectMultiple(),
    #         required=True,
    #         label='Sexo',
    #     )

class eventoForm(forms.Form):
    
    MASCOTAS = []
    records = consultar_mascotas()
    for row in records:
        MASCOTAS.append(row[1])
        MASCOTAS.append(row[1])

    mascotas = forms.ChoiceField(label="mascotas", choices=[MASCOTAS])

    descripcion = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "descripcion",
                "class": "form-control"
            }
        ))
    OPTIONS = [
        ("1", "Esterilización"),
        ("2", "Microchip"),
        ("3", "Consulta")
        ]

    tipo_evento = forms.ChoiceField(
            choices=OPTIONS,
            initial='0',
            required=True,
            label='Tipo de consulta',
        )
