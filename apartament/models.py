from django.db import models


class ObjectApartament(models.Model):
    name = models.CharField(max_length=100, verbose_name='Объект')

    class Meta:
        verbose_name = 'Объект'
        verbose_name_plural = 'Объекты'

    def __str__(self):
        return self.name


class Apartment(models.Model):
    STATUS_CHOICES = [
        ('bron', 'Бронь'),
        ('purchased', 'Куплено'),
        ('barter', 'Бартер'),
        ('instalment', 'Рассрочка'),
        ('cancel', 'Отмена'),
        ('active', 'Активна'),
    ]

    number_apartament = models.IntegerField(verbose_name='№ Квартиры')
    apartament_object = models.ForeignKey(
        ObjectApartament,
        on_delete=models.CASCADE,
        related_name = 'apartament',
        verbose_name='Объект'
    )
    floor = models.IntegerField(verbose_name='Этаж')
    area = models.DecimalField(max_digits=10, decimal_places=1, verbose_name='КВ')
    date = models.DateField(verbose_name='Дата')
    status = models.CharField(max_length=30, choices=STATUS_CHOICES, verbose_name='Статус')
    price = models.IntegerField(verbose_name='Цена')
    client = models.CharField(max_length=100, verbose_name='Клиент')
    status_apartment = models.DateTimeField(verbose_name='Статус')

    def get_status_display(self):
        for code, name in self.STATUS_CHOICES:
            if code == self.status:
                return name
        return None

    class Meta:
        verbose_name = 'Квартира'
        verbose_name_plural = 'Квартиры'

