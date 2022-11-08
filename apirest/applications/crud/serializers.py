from rest_framework import serializers, pagination

from .models import Persona

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Persona
        fields = ('__all__')
