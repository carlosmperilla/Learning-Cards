from django.contrib import admin
from .models import Card

class CardAdmin(admin.ModelAdmin):
    readonly_fields =  (
                    'hits',
                    'mistakes',
                    )
    list_display = (
                    'pk',
                    'foreign_word',
                    'native_word',
                    'hits',
                    'mistakes',
                    'kit_name',
                    'user_name',
                    )
    search_fields = (
                    'foreign_word',
                    'native_word',
                    'kit__name',
                    'kit__user__username',
                    )
    ordering = (
                'kit__user__username',
                'kit__name',
                'foreign_word',
                'native_word',
                )
    list_filter = (
                    'kit__user__username',
                    'kit__name',
                    )

    
    def kit_name(self, obj):
        return f"{obj.kit.pk} - {obj.kit.name}"

    def user_name(self, obj):
        return obj.kit.user.username

    kit_name.short_description = "Pk - Kit"
    user_name.short_description = "Usuario"

# Register your models here.
admin.site.register(Card, CardAdmin)
