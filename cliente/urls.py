from django.urls import path
from .views import client_list

urlpatterns = [
    path('list/', client_list, name="client_list"),
]