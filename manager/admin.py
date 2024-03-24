from django.contrib import admin
from manager.models import Manager


@admin.register(Manager)
class ManagerAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'phone_number', 'created_at')
    list_display_links = ('id', 'full_name', 'phone_number')

    fields = ('id', 'full_name', 'phone_number', 'created_at')
    readonly_fields = ('id', 'created_at')