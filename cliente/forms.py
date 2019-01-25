from django.forms import ModelForm
from .models import Cliente

class ClientForm(ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome_cliente']