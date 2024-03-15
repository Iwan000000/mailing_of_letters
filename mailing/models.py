from django.conf import settings
from django.db import models

NULLABLE = {'blank': True, 'null': True}


class Mailing(models.Model):
    """
    Модель для рассылок
    """
    TIME_CHOICES = [
        ('daily', 'Раз в день'),
        ('weekly', 'Раз в неделю'),
        ('monthly', 'Раз в месяц'),
    ]

    name = models.CharField(max_length=50, verbose_name='Имя рассылки', **NULLABLE)
    data_mailing = models.DateTimeField(verbose_name='Дата и время отправки')
    data_mailing_finish = models.DateTimeField(verbose_name='Дата и время окончания рассылки', **NULLABLE)
    periodicity = models.CharField(max_length=20, choices=TIME_CHOICES, verbose_name='Периодичность рассылки')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, **NULLABLE, verbose_name='ID клиента')
    status = models.CharField(max_length=50, verbose_name='Status mailing', **NULLABLE)

    def __str__(self):
        return f'{self.pk}'

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
