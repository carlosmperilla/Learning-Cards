
import string
from statistics import mean

from django.contrib.auth.models import User

from django.db import models
from django.db.models.signals import pre_save
from django.core.validators import MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

from card.models import Card

# Create your models here.
class Kit(models.Model):
    name = models.CharField(blank=False, null=False, max_length=50, verbose_name="Nombre")
    foreign_language = models.CharField(blank=False, null=False, max_length=20, verbose_name="Idioma Foraneo")
    native_language = models.CharField(blank=False, null=False, max_length=20, verbose_name="Idioma Nativo")
    added_date =  models.DateTimeField(auto_now_add=True, verbose_name="Creado el")
    successful = models.IntegerField(default=0, verbose_name="Ratio de exito", validators=[MinValueValidator(0), MaxValueValidator(100)])
    user = models.ForeignKey(User, editable=True, verbose_name='Usuario', on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Kit"
        verbose_name_plural = "Kits"
        ordering = ['name']

    def __str__(self):
        return self.name + ' - ' + str(self.pk)

    def generate_cards(self, kit_file):
        """
            Generates the letters associated with the language kit.
        """
        cards = []
        foreign_words = []
        for line in kit_file.readlines():
            clean_line = line.strip()
            if clean_line.decode('utf-8') in string.whitespace:
                continue
            words = clean_line.decode('utf-8').split(':')[:2]
            foreign_word = words[0].strip()[:51]
            native_word = words[1].strip()[:51]
            if foreign_word in foreign_words:
                continue
            foreign_words.append(foreign_word)
            cards.append(Card(foreign_word = foreign_word, native_word = native_word, kit=self))
        kit_file.close()
        Card.objects.bulk_create(cards)

    def put_successful(self):
        """
            Calculate and update the value of successful
        """
        self.successful = round(mean(success_value[0] for success_value in self.cards.values_list('success')))
        self.save(update_fields=['successful'])

def unique_name_per_user(sender, instance, *args, **kwargs):
    """
        Verify that the stock name is unique per user.
    """
    # print(instance.lc_lang)
    lc_lang = getattr(instance, 'lc_lang', None)
    kit_by_user = sender.objects.filter(user__pk=instance.user.pk)
    kits_by_name = kit_by_user.filter(name=instance.name)
    if kits_by_name.exists():
        if not instance == kits_by_name.first():
            if lc_lang == "es":
                raise ValidationError("UNPS - Nombre de Kit ya registrado previamente.")
            else:
                raise ValidationError("UNPS - Kit name already registered previously.")


pre_save.connect(unique_name_per_user, sender=Kit)