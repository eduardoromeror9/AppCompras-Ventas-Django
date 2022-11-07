from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class ClaseModelo(models.Model):
    estado = models.BooleanField(default=True)
    fc = models.DateTimeField(auto_now_add=True)  # Fecha de creacion(fc)
    fm = models.DateTimeField(auto_now=True)  # Fecha de modification(fm)
    uc = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario de creacion(uc)
    um = models.IntegerField(blank=True, null=True)  # Usuario de modification(um)

    class Meta:
        abstract = True

