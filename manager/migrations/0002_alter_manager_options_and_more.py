# Generated by Django 5.0.3 on 2024-03-24 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='manager',
            options={'verbose_name': 'Менеджер', 'verbose_name_plural': 'Менеджеры'},
        ),
        migrations.AlterField(
            model_name='manager',
            name='count_transaction',
            field=models.IntegerField(default=0, null=True, verbose_name='Количество сделок'),
        ),
    ]
