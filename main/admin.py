from django.contrib import admin

from article.models import Article
from client.models import Client
from mailing.models import Mailing
from message.models import Message
from users.models import User


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name', 'email', 'is_manager')


@admin.register(Mailing)
class MailingAdmin(admin.ModelAdmin):
    list_display = ('pk', 'data_mailing',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'mailing')


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'mailing')


@admin.register(Article)
class UserAdmin(admin.ModelAdmin):
    list_display = ('slug', 'title', 'text', 'blog_image', 'is_published')
