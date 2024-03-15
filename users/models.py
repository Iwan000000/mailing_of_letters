from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'blank': True, 'null': True}


# Create your models here.
class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name='электронная почта')
    name = models.CharField(max_length=50, verbose_name='Имя', **NULLABLE)
    lastname = models.CharField(max_length=50, verbose_name='Фамилия', **NULLABLE)
    company = models.CharField(max_length=50, verbose_name='Компания', **NULLABLE)
    avatar = models.ImageField(upload_to='users', **NULLABLE)
    phone = models.CharField(max_length=35, verbose_name='Номер телефона', **NULLABLE)
    country = models.CharField(max_length=50, verbose_name='Страна', **NULLABLE)
    birthday = models.DateField(verbose_name='День рождения', **NULLABLE)
    comment = models.CharField(max_length=300, verbose_name='Комментарий', **NULLABLE)
    is_manager = models.BooleanField(default=False)
    email_verify = models.BooleanField(default=False)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
