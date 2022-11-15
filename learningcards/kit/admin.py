from django.contrib import admin
from .models import Kit
from card.models import Card

class CardInline(admin.TabularInline):
    model = Card
    extra = 3

class KitAdmin(admin.ModelAdmin):
    readonly_fields =  (
                    'successful',
                    )
    list_display = (
                    'name',
                    'foreign_language',
                    'native_language',
                    'successful',
                    'user',
                    )
    search_fields = (
                    'name',
                    'foreign_language',
                    'native_language',
                    'successful',
                    'user__username',
                    )
    ordering = (
                'user__username', 
                'name',
                'foreign_language',
                'native_language',
                'successful',
                )
    list_filter = (
                    'user__username',
                    'name',
                    'foreign_language',
                    'native_language',
                    'successful',
                    )
    inlines = (
                CardInline,
                )

# Register your models here.
admin.site.register(Kit, KitAdmin)