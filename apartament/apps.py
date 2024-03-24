from django.apps import AppConfig


class ApartamentConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'apartament'
    verbose_name = 'Квартира'
    verbose_name_plural = 'Квартиры'
