# Generated by Django 4.2.3 on 2023-07-23 11:51

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Signup",
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
                ("username", models.CharField(blank=True, max_length=50, null=True)),
                ("first_name", models.CharField(blank=True, max_length=40, null=True)),
                ("last_name", models.CharField(blank=True, max_length=30, null=True)),
                ("email", models.EmailField(max_length=254)),
                (
                    "phone_number",
                    models.CharField(blank=True, max_length=12, null=True),
                ),
                ("password1", models.CharField(blank=True, max_length=50, null=True)),
                ("password2", models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]
