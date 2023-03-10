# Generated by Django 4.1.7 on 2023-03-01 09:46

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0012_rename_blogger_profile"),
    ]

    operations = [
        migrations.CreateModel(
            name="Profil",
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
        migrations.DeleteModel(
            name="Profile",
        ),
    ]
