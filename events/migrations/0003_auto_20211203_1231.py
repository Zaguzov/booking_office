# Generated by Django 2.2.6 on 2021-12-03 12:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0002_auto_20211203_1231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='location',
            name='artists',
            field=models.ManyToManyField(blank=True, to='events.Artist', verbose_name='Выступающие'),
        ),
    ]
