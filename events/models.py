from django.db import models
from django.contrib.auth import get_user_model
from django.core.validators import MinValueValidator

User = get_user_model()


class Event(models.Model):
    name = models.CharField(verbose_name='Название мероприятия',
                            max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=10000)
    kind = models.ForeignKey('EventKind', on_delete=models.CASCADE,
                             related_name='events',
                             verbose_name='Вид мероприятия')
    location = models.ForeignKey('Location', on_delete=models.CASCADE,
                                 related_name='events',
                                 verbose_name='Место проведения')
    start_date = models.DateTimeField(verbose_name='Дата и время '
                                                   'начала мероприятия')
    end_date = models.DateTimeField(verbose_name='Дата и время '
                                                 'окончания мероприятия')
    image = models.ImageField(upload_to='events/', blank=True, null=True,
                              verbose_name="Картинка к событию",
                              help_text="Загрузить выбранную")
    artists = models.ManyToManyField('Artist', verbose_name='Выступающие')
    pub_date = models.DateTimeField(verbose_name="Дата публикации",
                                    auto_now_add=True,
                                    help_text="Автоматически заполняется "
                                              "сегодняшней датой")

    class Meta:
        ordering = ["-pub_date"]
        verbose_name = 'События'
        verbose_name_plural= verbose_name

    def __str__(self):
        return self.name


class Location(models.Model):
    name = models.CharField(verbose_name='Название площадки', max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=10000)
    address = models.CharField(verbose_name='Адрес площадки', max_length=200)
    artists = models.ManyToManyField('Artist', verbose_name='Выступающие',
                                     blank=True)
    image = models.ImageField(upload_to='events/', blank=True, null=True,
                              verbose_name="Картинка к площадке",
                              help_text="Загрузить выбранную")

    class Meta:
        verbose_name = 'Место'
        verbose_name_plural= 'Места'
        
    def __str__(self):
        return self.name


class EventKind(models.Model):
    name = models.CharField(verbose_name='Название вида события',
                            max_length=100)
    description = models.TextField(verbose_name='Описание', max_length=1000)

    class Meta:
        verbose_name = 'Вид события'
        verbose_name_plural= 'Виды событий'
    
    def __str__(self):
        return self.name


class Artist(models.Model):
    initials = models.CharField(verbose_name='ФИО', max_length=200)
    description = models.TextField(verbose_name='Описание', max_length=10000)
    image = models.ImageField(upload_to='events/', blank=True, null=True,
                              verbose_name="Фотография",
                              help_text="Загрузить выбранную")

    class Meta:
        verbose_name = 'Выступающие'
        verbose_name_plural= verbose_name
        
    def __str__(self):
        return self.initials


class Tickets(models.Model):
    price = models.IntegerField(verbose_name='Цена за билет')
    number_of_available_tickets = models.IntegerField(verbose_name='Кол-во'
                                                                   ' доступных'
                                                                   ' билетов',
                                                      validators=
                                                      [MinValueValidator(1)])
    event = models.ForeignKey(Event, verbose_name='Событие',
                              related_name='tickets', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Билеты'
        verbose_name_plural= verbose_name
    
    def __str__(self):
        return self.event.name

class ShoppingCart(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Пользователь'
    )   
    ticket = models.ForeignKey(
        Tickets,
        on_delete=models.CASCADE,
        related_name='shopping_cart',
        verbose_name='Билет'
    )
    number_of_purchased_tickets = models.IntegerField(verbose_name='Кол-во'
                                                                   ' купленных'
                                                                   ' билетов',
                                                      validators=
                                                      [MinValueValidator(1)]
                                                      )
    class Meta:
        verbose_name = 'Покупки'
        verbose_name_plural= verbose_name
