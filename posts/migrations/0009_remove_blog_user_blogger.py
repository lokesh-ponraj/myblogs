# Generated by Django 4.1.7 on 2023-03-01 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0008_delete_blogger"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="user",
        ),
        migrations.CreateModel(
            name="Blogger",
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
                ("firstname", models.TextField()),
                ("lastname", models.TextField()),
                ("email", models.EmailField(max_length=254)),
                (
                    "blogs",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="posts.blog"
                    ),
                ),
                (
                    "username",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]