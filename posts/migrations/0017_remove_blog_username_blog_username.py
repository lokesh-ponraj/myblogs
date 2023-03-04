# Generated by Django 4.1.7 on 2023-03-02 05:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("posts", "0016_alter_blog_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="blog",
            name="username",
        ),
        migrations.AddField(
            model_name="blog",
            name="userName",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to=settings.AUTH_USER_MODEL,
            ),
        ),
    ]
