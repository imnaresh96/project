# Generated by Django 4.1.7 on 2023-03-06 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dellApp", "0002_user_profile"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_profile",
            name="Mobile",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]