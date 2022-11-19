from django.contrib import admin
from .models import TemplateTranslation, ElementTranslation

class ElementTranslationInline(admin.TabularInline):
    # model = ElementTranslation
    model = ElementTranslation.templatetranslation.through
    extra = 3

class TemplateTranslationAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    'view',
                    'is_user_authenticated',
                    )
    search_fields = (
                    'name',
                    'view',
                    )
    ordering = (
                'name',
                'view',
                'is_user_authenticated',
                )
    list_filter = (
                    'name',
                    'view',
                    'is_user_authenticated',
                    )
    inlines = (
                ElementTranslationInline,
                )

class ElementTranslationAdmin(admin.ModelAdmin):
    list_display = (
                    'name',
                    )
    search_fields = (
                    'name',
                    )
    ordering = (
                'name',
                )

# Register your models here.
admin.site.register(TemplateTranslation, TemplateTranslationAdmin)
admin.site.register(ElementTranslation, ElementTranslationAdmin)