from django.contrib import admin
from .models import Car


class CarAdmin(admin.ModelAdmin):
    list_display = ('make', 'model', 'display_image', 'display_link')

    def display_image(self, obj):
        return '<img src="%s" width="50" height="50" />' % obj.image.url

    def display_link(self, obj):
        return '<a href="%s">%s</a>' % (obj.link, obj.link)

    display_image.allow_tags = True
    display_link.allow_tags = True
    display_image.short_description = 'Image'
    display_link.short_description = 'Link'


admin.site.register(Car, CarAdmin)