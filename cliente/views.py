from django.urls import reverse
from .models import Cliente
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import ClientForm
from django.views.generic import (
    ListView,
    CreateView,
)
from django.views.generic.edit import UpdateView

# Listar clientes
class ClientList(ListView):
    clients = Cliente.objects.all()

    def get_queryset(self, *args, **kwargs):
        # queryset = Tarefa.objects.filter(user=self.request.user)
        return Cliente.objects.filter(user=self.request.user)

# Cadastrar clientes
class CriaCliente(CreateView):
    template_name = 'cliente/cliente_create_form.html'
    form_class = ClientForm

    #@method_decorator(login_required)
    def dispatch(self, *args, **kwargs):
        return super(CriaCliente, self).dispatch(*args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('client_list')

# Update clientes
class UpdateCliente(UpdateView):
    model = Cliente
    fields = ['nome_cliente']
    pk_url_kwarg = 'id'
    #success_url = '../client_list'
    def get_success_url(self):
        return reverse('client_list')