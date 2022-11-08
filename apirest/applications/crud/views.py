from django.shortcuts import render

# Create your views here.
from django.views.generic import ListView
from rest_framework.generics import ListAPIView
from .models import Persona
from .serializers import PersonSerializer


class PersonaListView(ListView):
    model = Persona
    template_name = "crud/lista.html"
    context_object_name = "lista"

class PersonListApiView(ListAPIView):

    serializer_class = PersonSerializer

    def get_queryset(self):
        return Persona.objects.all()