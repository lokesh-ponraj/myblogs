# Generated by Django 4.1.7 on 2023-02-24 06:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("posts", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Blog",
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
                ("user", models.CharField(max_length=50)),
                (
                    "category",
                    models.CharField(
                        choices=[
                            ("Frontend", "Frontend"),
                            ("Backend", "Backend"),
                            ("Career", "Career"),
                            ("Database", "Database"),
                            ("Frameworks", "Frameworks"),
                            ("Github", "Github"),
                            ("Hackathons", "Hackathons"),
                            ("Languages", "Languages"),
                        ],
                        max_length=50,
                    ),
                ),
                ("heading", models.CharField(max_length=100)),
                ("description", models.CharField(max_length=50)),
                ("content", models.TextField()),
                ("date", models.DateField(auto_now=True)),
            ],
        ),
        migrations.DeleteModel(
            name="Frontend",
        ),
    ]
