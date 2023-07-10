from django import forms
from .models import Cliente, Producto, Auto, ImagenAuto
from django.contrib.auth.forms import UserCreationForm
from datetime import date

class ContactoForm(forms.ModelForm):
    # con meta para decile a que modelo esta relacionaod para que tome los campos
    class Meta:
        model = Cliente
        # si quiero que liste todo pongo
        fields = '__all__'
        # fields = ["nombre", "run", "celular","email"]

class ProductoForm(forms.ModelForm):

    imagen = forms.ImageField(required=False)
    fecha_creacion = initial=date.today()

    class Meta:
        model = Producto
        fields = '__all__'

        widgets = {
            

            "fecha_creacion": forms.DateInput(attrs={'class': 'datepicker'})
        }


class AutoForm(forms.ModelForm):

    imagen = forms.ImageField(required=False)

    class Meta:
        model = Auto
        fields = '__all__'

        


class CustomUserCreationForm(UserCreationForm):
    pass
