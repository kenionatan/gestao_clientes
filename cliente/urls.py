from django.urls import path
from .views import ClientList

urlpatterns = [
    path('list/', ClientList.as_view()),
]