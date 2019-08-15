from django.contrib import admin
from indexpage import models


# Register your models here.
class BlockAdmin(admin.ModelAdmin):
    list_display = ['order', 'title', 'subtitle']
    search_fields = ['order', 'title', 'subtitle', 'content']


class ItemAdmin(admin.ModelAdmin):
    list_display = ['order', 'title']
    search_fields = ['order', 'title', 'content']


class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'metadescr', 'metakeywords']
    search_fields = ['title', 'metadescr', 'metakeywords']


admin.site.register(models.Block, BlockAdmin)
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Settings, SettingsAdmin)
