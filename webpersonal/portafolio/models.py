from django.db import models

class Portafolio(models.Model):
    title = models.CharField(max_length=255, verbose_name='Título')
    image = models.ImageField(upload_to='projects', verbose_name='Imagen')
    description = models.TextField(max_length=500, verbose_name='Descripción')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Creado el')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='Editado el')
    url = models.URLField(blank=True, null=True, verbose_name='Url')

    class Meta:
        verbose_name = 'Proyecto'
        verbose_name_plural = 'Proyectos'
        ordering = ['-created_at']

    def __str__(self):
        return self.title