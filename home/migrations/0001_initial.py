# Generated by Django 4.1 on 2022-10-07 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Gujarat_hospital",
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
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("address", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=20)),
                ("link", models.CharField(default="#", max_length=100)),
                (
                    "img",
                    models.ImageField(
                        default="default.jpg", upload_to="gujarat_hospital"
                    ),
                ),
                ("city", models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name="Gujarat_Ngo",
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
                ("title", models.CharField(max_length=100)),
                ("content", models.TextField()),
                ("address", models.CharField(max_length=100)),
                ("phone_number", models.CharField(max_length=20)),
                ("link", models.CharField(default="#", max_length=100)),
                (
                    "img",
                    models.ImageField(default="default.jpg", upload_to="gujarat_Ngo"),
                ),
                ("city", models.CharField(max_length=30)),
            ],
        ),
    ]
