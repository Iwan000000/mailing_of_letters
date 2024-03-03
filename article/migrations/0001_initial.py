# Generated by Django 4.2.7 on 2024-03-01 17:08

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Article",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("title", models.CharField(max_length=150, verbose_name="title")),
                (
                    "slug",
                    models.CharField(
                        blank=True, max_length=150, null=True, verbose_name="slug"
                    ),
                ),
                ("text", models.TextField(verbose_name="text")),
                (
                    "blog_image",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="article/",
                        verbose_name="article_image",
                    ),
                ),
                (
                    "data_created",
                    models.DateField(default="2023-01-01", verbose_name="Data created"),
                ),
                (
                    "data_published",
                    models.DateField(
                        default="2023-01-01", verbose_name="Data published"
                    ),
                ),
                (
                    "number_views",
                    models.IntegerField(default=0, verbose_name="number of views"),
                ),
                ("is_published", models.BooleanField(default=True)),
            ],
            options={
                "verbose_name": "article",
                "verbose_name_plural": "articles",
            },
        ),
    ]
