from django.contrib import admin
from indexpage import models

# Register your models here.
class BlockAdmin(admin.ModelAdmin):
    list_display = ['pk', ]


class ItemAdmin(admin.ModelAdmin):
    list_display = ['pk']

class SettingsAdmin(admin.ModelAdmin):
    list_display = ['pk']

admin.site.register(models.Block, BlockAdmin)
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Settings, SettingsAdmin)