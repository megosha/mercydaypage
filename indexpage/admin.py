from django.contrib import admin
from indexpage import models


# Register your models here.
class BlockAdmin(admin.ModelAdmin):
    list_display = ['order', 'title', 'subtitle', 'picture', 'content']
    list_display_links = ['order', 'title']
    list_editable = ['subtitle', 'content']
    list_filter = ['picture']
    search_fields = ['title', 'subtitle']
    save_on_top = True



class ItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'content']
    search_fields = ['order', 'title', 'content']
    list_display_links = ['title']
    list_editable = ['content']
    save_on_top = True



class SettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'date', 'phone', 'email', 'metadescr', 'metakeywords']
    # search_fields = ['phone', 'email',]
    list_display_links = ['title']
    list_editable = ['phone', 'email', 'date']
    # readonly_fields = 'registry',

admin.site.register(models.Block, BlockAdmin)
admin.site.register(models.Item, ItemAdmin)
admin.site.register(models.Settings, SettingsAdmin)
