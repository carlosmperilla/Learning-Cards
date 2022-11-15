
from django.contrib.auth.models import User

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Kit(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre")
    foreign_language = models.CharField(max_length=20, verbose_name="Idioma Foraneo")
    native_language = models.CharField(max_length=20, verbose_name="Idioma Nativo")
    added_date =  models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    successful = models.IntegerField(default=0, verbose_name="Ratio de exito", validators=[MinValueValidator(0), MaxValueValidator(100)])
    user = models.ForeignKey(User, editable=True, verbose_name='Usuario', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Kit"
        verbose_name_plural = "Kits"
        ordering = ['name']

    def __str__(self):
        return self.name + ' - ' + str(self.pk)