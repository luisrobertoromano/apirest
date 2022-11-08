from django.db import models

# Create your models here.

class Persona(models.Model):
    """Model definition for Persona."""

    apellido = models.CharField("Apellido", max_length=50)
    nombre = models.CharField("Nombre", max_length=50)
    dni = models.CharField("DNI", max_length=50, unique=True)

    class Meta:
        """Meta definition for Persona."""

        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

    def __str__(self):
        """Unicode representation of Persona."""
        return self.apellido + ", " + self.nombre
