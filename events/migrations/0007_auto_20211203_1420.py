# Generated by Django 2.2.6 on 2021-12-03 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0006_auto_20211203_1415'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='artist',
            options={'verbose_name': 'Выступающие', 'verbose_name_plural': 'Выступающие'},
        ),
        migrations.AlterModelOptions(
            name='eventkind',
            options={'verbose_name': 'Вид события', 'verbose_name_plural': 'Виды событий'},
        ),
        migrations.AlterModelOptions(
            name='location',
            options={'verbose_name': 'Место', 'verbose_name_plural': 'Места'},
        ),
        migrations.AlterModelOptions(
            name='shoppingcart',
            options={'verbose_name': 'Покупки', 'verbose_name_plural': 'Покупки'},
        ),
        migrations.AlterModelOptions(
            name='tickets',
            options={'verbose_name': 'Билеты', 'verbose_name_plural': 'Билеты'},
        ),
    ]
