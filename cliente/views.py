from django.shortcuts import render
from .models import Cliente

def client_list(request):
    clients = Cliente.objects.all()
    return render(request, 'clientes.html', {'clients': clients})
