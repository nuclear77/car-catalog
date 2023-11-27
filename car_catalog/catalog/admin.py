from django.contrib import admin
from django.utils.html import format_html
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'display_image', 'display_link')
    readonly_fields = ('display_image',)

    def display_image(self, obj):
        return format_html('<img src="{}" width="100" height="100" />', obj.image.url)

    def display_link(self, obj):
        return format_html('<a href="{}">{}</a>', obj.link, obj.link)

    display_image.short_description = 'Image'
    display_link.short_description = 'Link'


admin.site.register(Car, CarAdmin)