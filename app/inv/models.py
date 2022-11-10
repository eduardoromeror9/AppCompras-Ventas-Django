from django.db import models
from bases.models import ClaseModelo


# Create your models here.
class Categoria(ClaseModelo):
    descripcion = models.CharField(
        max_length=100,
        help_text='Descripcion de la categoria',
        unique=True
    )

    def __str__(self):
        return f'{self.descripcion}'

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Categoria, self).save()

    class Meta:
        verbose_name_plural = 'Categorias'
        

class SubCategoria(ClaseModelo):
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    descripcion = models.CharField(
        max_length = 100,
        help_text = 'Descripcion de la subcategoria',
    )

    def __str__(self):
        return f'{self.categoria.descripcion}:{self.descripcion}'

    def save(self):
        self.descripcion = self.descripcion.upper()
        super(SubCategoria, self).save()

    class Meta:
        verbose_name_plural = 'Subcategorias'
        unique_together = ('categoria', 'descripcion')
        

class Marca(ClaseModelo):
    descripcion = models.CharField(
        max_length = 100,
        help_text = 'Descripcion de la Marca',
        unique = True
    )
    
    def __str__(self):
        return f'{self.descripcion}'
    
    def save(self):
        self.descripcion = self.descripcion.upper()
        super(Marca, self).save()
        
    class Meta:
        verbose_name_plural = 'Marcas'