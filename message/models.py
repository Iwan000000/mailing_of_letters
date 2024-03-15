from django.db import models

from mailing.models import Mailing

NULLABLE = {'blank': True, 'null': True}


# Create your models here.


class Message(models.Model):
    """
    Модель для сообщений.
    """
    title = models.CharField(max_length=50, verbose_name='Заголовок')
    body = models.TextField(verbose_name='Тело сообщения')
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Почтовый идентификатор')

    def __str__(self):
        return f'{self.title}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
