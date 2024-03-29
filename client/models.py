from django.db import models

from mailing.models import Mailing

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class Client(models.Model):
    """
    Модель для клиентов
    """
    name = models.CharField(max_length=50, verbose_name='Имя')
    lastname = models.CharField(max_length=50, verbose_name='Фамилия')
    birthday = models.DateField(verbose_name='День рождения', **NULLABLE)
    email = models.EmailField(max_length=50, verbose_name='Электронная почта')
    comment = models.CharField(max_length=300, verbose_name='Комментарий', **NULLABLE)
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE, verbose_name='Почтовый идентификатор')

    def __str__(self):
        return f'{self.name} {self.lastname}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'
