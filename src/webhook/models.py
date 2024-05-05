from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone


class User(AbstractUser):
    tg_chat_id = models.TextField(max_length=20, blank=True, null=True)
    send_notification = models.BooleanField(default=False)


class Event(models.Model):
    date = models.DateField('Дата события', default=timezone.now)
    name = models.CharField('Имя', max_length=40)
    thumbnail = models.ImageField('Превью')
    full_frame = models.ImageField('Полноразмерное фото')

    def __str__(self):
        return f'{self.date} - {self.name}'

    class Meta:
        verbose_name = 'Событие'
        verbose_name_plural = 'События'
