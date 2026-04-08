from django.contrib import admin
from .models import Save

@admin.register(Save)
class SaveAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    readonly_fields = ['id', 'name']
