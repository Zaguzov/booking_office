# Generated by Django 2.2.6 on 2021-12-03 12:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('initials', models.CharField(max_length=200, verbose_name='ФИО')),
                ('description', models.TextField(max_length=10000, verbose_name='Описание')),
                ('image', models.ImageField(blank=True, help_text='Загрузить выбранную', null=True, upload_to='events/', verbose_name='Фотография')),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название мероприятия')),
                ('description', models.TextField(max_length=10000, verbose_name='Описание')),
                ('start_date', models.DateTimeField(verbose_name='Дата и время начала мероприятия')),
                ('end_date', models.DateTimeField(verbose_name='Дата и время окончания мероприятия')),
                ('image', models.ImageField(blank=True, help_text='Загрузить выбранную', null=True, upload_to='events/', verbose_name='Картинка к событию')),
                ('pub_date', models.DateTimeField(auto_now_add=True, help_text='Автоматически заполняется сегодняшней датой', verbose_name='Дата публикации')),
                ('artists', models.ManyToManyField(to='events.Artist', verbose_name='Выступающие')),
            ],
            options={
                'ordering': ['-pub_date'],
            },
        ),
        migrations.CreateModel(
            name='EventKind',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название вида события')),
                ('description', models.TextField(max_length=1000, verbose_name='Описание')),
            ],
        ),
        migrations.CreateModel(
            name='Tickets',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField(verbose_name='Цена за билет')),
                ('place', models.CharField(max_length=100, verbose_name='Место на площадке')),
                ('number_of_available_tickets', models.IntegerField(verbose_name='Кол-во доступных билетов')),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='tickets', to='events.Event', verbose_name='Событие')),
            ],
        ),
        migrations.CreateModel(
            name='ShoppingCart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number_of_purchased_tickets', models.IntegerField(verbose_name='Кол-во купленных билетов')),
                ('ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart', to='events.Tickets', verbose_name='Билет')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='shopping_cart', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название площадки')),
                ('description', models.TextField(max_length=10000, verbose_name='Описание')),
                ('address', models.CharField(max_length=200, verbose_name='Адрес площадки')),
                ('image', models.ImageField(blank=True, help_text='Загрузить выбранную', null=True, upload_to='events/', verbose_name='Картинка к площадке')),
                ('artists', models.ManyToManyField(to='events.Artist', verbose_name='Выступающие')),
            ],
        ),
        migrations.AddField(
            model_name='event',
            name='kind',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='events.EventKind', verbose_name='Вид мероприятия'),
        ),
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='events', to='events.Location', verbose_name='Место проведения'),
        ),
    ]
