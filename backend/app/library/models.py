from django.db import models

# Create your models here.

class Libros(models.Model):
    nombre = models.CharField(max_length=60, verbose_name='Nombre del libro')
    autor = models.CharField(max_length=250, verbose_name='Nombre del autor')
    isbn = models.IntegerField(default=0, verbose_name='ISBN')
    edicion = models.IntegerField(default=1, verbose_name='Número de edición')
    fecha_pub = models.DateField(verbose_name='Fecha de publicación')
    creado = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    status_delete = models.BooleanField(default=False)

    class Meta:
        db_table = 'libros'