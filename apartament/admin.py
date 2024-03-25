from django.contrib import admin
from apartament.models import Apartment, ObjectApartament


@admin.register(Apartment)
class ApartmentAdmin(admin.ModelAdmin):
    list_display = ('id', 'number_apartament', 'apartament_object', 'area')
    list_display_links = ('id', 'number_apartament', 'apartament_object', 'area')



@admin.register(ObjectApartament)
class ObjectApartamentAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')