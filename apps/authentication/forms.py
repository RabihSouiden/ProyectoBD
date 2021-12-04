from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.forms import fields
from . import models


class LoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Usuario",
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control"
            }
        ))


class SignUpForm(UserCreationForm):
    username = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Usuario",
                "class": "form-control"
            }
        ))
    first_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre",
                "class": "form-control"
            }
        ))
    last_name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Apellido",
                "class": "form-control"
            }
        ))
    num_documento = forms.IntegerField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Número de documento",
                "class": "form-control"
            }
        ))
    OPTIONS = [
        ("1", "Cédula Ciudadania"),
        
        ]
    tipo_documento = forms.ChoiceField(
            choices=OPTIONS,
            initial='0',
            required=True,
            label='Tipo documento',
        )
    OPTIONS_USUARIO = [
        ("1","Propietario"),
        ("2", "Veterinaria")
    ]
    tipo_usuario = forms.ChoiceField(
            choices=OPTIONS_USUARIO,
            initial='0',
            required=True,
            label='Tipo usuario',
        )
    direccion_usuario = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Dirección",
                "class": "form-control"
            }
        ))
    barrio_usuario = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Barrio",
                "class": "form-control"
            }
        ))
    telefono_usuario = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Telefono",
                "class": "form-control"
            }
        ))
    localidad_usuario = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Localidad",
                "class": "form-control"
            }
        ))
    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Correo",
                "class": "form-control"
            }
        ))
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Contraseña",
                "class": "form-control"
            }
        ))
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder": "Repita la contraseña",
                "class": "form-control"
            }
        ))

    class Meta:
        model = models.CustomUsers
        #fields = ('password1', 'username', 'first_name','last_name','email','num_documento', 'tipo_documento','tipo_usuario','username','telefono_usuario','email','password1','direccion_usuario','barrio_usuario','localidad_usuario')
        fields = ('num_documento','tipo_documento','tipo_usuario','username','telefono_usuario','email','password1','direccion_usuario','barrio_usuario','localidad_usuario','first_name','last_name')