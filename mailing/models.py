from django.db import models
from django.conf import settings
from users.models import User

NULLABLE = {'blank': True, 'null': True }


class Periodicity(models.Model):
    """
    Модель периодичности рассылки.
    """
    vars = models.CharField(max_length=50, verbose_name='Варианты периодичности')

    def __str__(self):
        return f'{self.vars}'

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Варианты'


class Mailing(models.Model):
    """
    Модель для рассылок
    """
    name = models.CharField(max_length=50, verbose_name='Имя рассылки', **NULLABLE)
    data_mailing = models.DateTimeField(verbose_name='Дата и время отправки')
    data_mailing_finish = models.DateTimeField(verbose_name='Дата и время окончания рассылки', **NULLABLE)
    periodicity = models.ForeignKey(Periodicity, on_delete=models.CASCADE, verbose_name='периодичность')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,  **NULLABLE, verbose_name='ID клиента')
    status = models.CharField(max_length=50, verbose_name='Status mailing', **NULLABLE)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
