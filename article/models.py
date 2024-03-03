from django.db import models
from pytils.translit import slugify
import datetime

NULLABLE = {'blank': True, 'null': True}


class Article(models.Model):
    title = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.CharField(max_length=150, verbose_name='slug', **NULLABLE)
    text = models.TextField(verbose_name='текст')
    blog_image = models.ImageField(upload_to='article/', **NULLABLE, verbose_name='изображение')
    data_created = models.DateField(verbose_name='Дата создания', default='2023-01-01')
    data_published = models.DateField(verbose_name='Дата опубликования', default='2023-01-01')
    number_views = models.IntegerField(verbose_name='количество просмотров', default=0)
    is_published = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'

    def save(self, *args, **kwargs):

        if not self.slug:
            self.slug = slugify(self.title)
        now = datetime.datetime.now()
        self.data_created = now
        self.data_published = now
        super().save(args, kwargs)

    class Meta:
        verbose_name = 'статья'
        verbose_name_plural = 'статьи'
