# Generated by Django 4.1.7 on 2023-02-25 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0003_alter_blog_description"),
    ]

    operations = [
        migrations.AddField(
            model_name="blog",
            name="imageAdd",
            field=models.CharField(default=True, max_length=500),
        ),
    ]
