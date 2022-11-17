from django.contrib import admin
from .models import TemplateTranslation, ElementTranslation

class ElementTranslationInline(admin.TabularInline):
    model = ElementTranslation
    extra = 3

class TemplateTranslationAdmin(admin.ModelAdmin):
    list_display = (
                    'view',
                    )
    search_fields = (
                    'view',
                    )
    ordering = (
                'view',
                )
    list_filter = (
                    'view',
                    )
    inlines = (
                ElementTranslationInline,
                )

# Register your models here.
admin.site.register(TemplateTranslation, TemplateTranslationAdmin)