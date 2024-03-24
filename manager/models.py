from django.db import models
from django.contrib.auth.models import User


class Manager(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='manager', verbose_name='Пользователь')
    full_name = models.CharField(max_length=200, verbose_name='ФИО')
    phone_number = models.CharField(max_length=15, verbose_name='Номер телефона')
    created_at = models.DateField(auto_now_add=True)
    count_transaction = models.IntegerField(default=0, null=True, verbose_name='Количество сделок')


    class Meta:
        verbose_name = 'Менеджер'
        verbose_name_plural = 'Менеджеры'

    def __str__(self):
        return self.full_name