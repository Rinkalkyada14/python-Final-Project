# Generated by Django 4.2.4 on 2023-09-01 07:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("artapp", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="profile_pic",
            field=models.ImageField(default="", upload_to="profile_pic/"),
        ),
    ]
