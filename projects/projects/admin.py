from django.contrib import admin

# Register your models here.
from .models import Component, File, Layer, Item, Project, Status, \
    Version

from django_mptt_admin.admin import DjangoMpttAdmin

class ComponentAdmin(DjangoMpttAdmin):
    pass


class FileAdmin(admin.ModelAdmin):
    pass


class LayerAdmin(admin.ModelAdmin):
    pass


class ItemAdmin(admin.ModelAdmin):
    pass


class ProjectAdmin(admin.ModelAdmin):
    pass


class StatusAdmin(admin.ModelAdmin):
    pass


class VersionAdmin(admin.ModelAdmin):
    pass


admin.site.register(Component, ComponentAdmin)
admin.site.register(File, FileAdmin)
admin.site.register(Layer, LayerAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(Version, VersionAdmin)
