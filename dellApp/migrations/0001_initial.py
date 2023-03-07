# Generated by Django 4.1.7 on 2023-03-03 12:13

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Master",
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
                ("Email", models.EmailField(max_length=254, unique=True)),
                ("Password", models.CharField(max_length=20)),
                ("IsActive", models.BooleanField(default=False)),
            ],
            options={"db_table": "Master",},
        ),
    ]