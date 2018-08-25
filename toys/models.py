from django.db import models

# Create your models here.

class Toy(models.Model):
    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de creación')
    name = models.CharField(max_length=150, blank=False, verbose_name='Nombre', default='')
    description = models.CharField(max_length=250, blank=True, default='', verbose_name='Descripción', \
                                   help_text="Este campo no es necesario pero ayuda a la descripción del juguete")
    toy_category = models.CharField(max_length=200, blank=False, default='', verbose_name='Categoría del juguete')
    release_date = models.DateTimeField(verbose_name='Fecha de liberación')
    was_included_in_home = models.BooleanField(default=False, verbose_name='Está incluido en el inicio')

    class Meta:
        verbose_name = 'juguete'
        verbose_name_plural = 'juguetes'
        ordering = ('id',)

    def __str__(self):
        return self.name