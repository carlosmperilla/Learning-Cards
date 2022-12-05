from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Card(models.Model):
    foreign_word = models.CharField(max_length=50, verbose_name="Palabra foranea")
    native_word = models.CharField(max_length=50, verbose_name="Palabra nativa")
    hits = models.IntegerField(default=0, verbose_name="Aciertos", validators=[MinValueValidator(0), MaxValueValidator(99999999)])
    mistakes = models.IntegerField(default=0, verbose_name="Errores", validators=[MinValueValidator(0), MaxValueValidator(99999999)])
    success = models.IntegerField(default=0, verbose_name="Ratio de exito", validators=[MinValueValidator(0), MaxValueValidator(100)])
    kit = models.ForeignKey('kit.Kit', editable=True, verbose_name='Kit', on_delete=models.CASCADE, related_name="cards")

    class Meta:
        verbose_name = "Card"
        verbose_name_plural = "Cards"
        ordering = ['foreign_word']

    def __str__(self):
        return self.foreign_word + ' - ' + self.native_word + ' - ' + str(self.pk)

    def put_success(self):
        """
            Calculate and update the value of success. And the new value of hits or mistakes.
        """
        new_success = (self.hits/(self.hits+self.mistakes))
        self.success = int(new_success*100)
        self.save(update_fields=['hits', 'mistakes', 'success'])