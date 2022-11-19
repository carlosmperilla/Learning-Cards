from django.db import models

# Create your models here.
class TemplateTranslation(models.Model):
    name = models.CharField(default="", max_length=50, verbose_name="Nombre de template") 
    view = models.CharField(default="", max_length=50, verbose_name="Nombre de vista")
    is_user_authenticated = models.BooleanField(default=False, verbose_name="¿Usuario autenticado?")

    class Meta:
        verbose_name = "Traducción de template"
        verbose_name_plural = "Traducciónes de templates"
        ordering = ['view']

    def __str__(self):
        return self.name + ' - ' + self.view + ' - ' + str(self.pk)

class ElementTranslation(models.Model):
    name = models.CharField(max_length=50, verbose_name="Nombre de elemento")
    selector = models.CharField(max_length=150, verbose_name="Selector CSS")
    spanish_text = models.CharField(max_length=1500, verbose_name="Texto en español")
    english_text = models.CharField(max_length=1500, verbose_name="Texto en inglés")
    templatetranslation = models.ManyToManyField('templatetranslation.TemplateTranslation', editable=True, verbose_name='Traducción de template', related_name="elementstranslation")

    class Meta:
        verbose_name = "Traducción de elemento"
        verbose_name_plural = "Traducciónes de elementos"
        ordering = ['name']

    def __str__(self):
        return self.name + ' - ' + str(self.pk)


    