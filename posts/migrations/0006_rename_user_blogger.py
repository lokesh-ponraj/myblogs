# Generated by Django 4.0.3 on 2023-02-27 11:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0005_user'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='User',
            new_name='Blogger',
        ),
    ]