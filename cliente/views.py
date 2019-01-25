from django.shortcuts import render
from .models import Cliente
from django.views.generic.list import ListView

class ClientList(ListView):
    clients = Cliente.objects.all()

    def get_queryset(self, *args, **kwargs):
        # queryset = Tarefa.objects.filter(user=self.request.user)
        return Cliente.objects.filter(user=self.request.user)
