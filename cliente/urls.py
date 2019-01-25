from django.urls import path
from .views import ClientList, CriaCliente, UpdateCliente

urlpatterns = [
    path('list/', ClientList.as_view(), name="client_list"),
    path('new/', CriaCliente.as_view(), name="client_new"),
    path('update/<int:id>', UpdateCliente.as_view(), name="client_update"),
]