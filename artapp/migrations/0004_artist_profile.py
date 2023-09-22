# Generated by Django 4.2.4 on 2023-09-04 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("artapp", "0003_user_usertype"),
    ]

    operations = [
        migrations.CreateModel(
            name="Artist_Profile",
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
                (
                    "artist_category",
                    models.CharField(
                        choices=[
                            ("Painter", "Painter"),
                            ("Singer", "Singer"),
                            ("Dancer", "Dancer"),
                            ("Comedian", "Comedian"),
                        ],
                        max_length=100,
                    ),
                ),
                ("artist_fees", models.PositiveIntegerField()),
                ("artist_desc", models.TextField()),
                ("picture1", models.ImageField(upload_to="artist_pic/")),
                ("picture2", models.ImageField(upload_to="artist_pic/")),
                ("picture3", models.ImageField(upload_to="artist_pic/")),
                (
                    "artist",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="artapp.user"
                    ),
                ),
            ],
        ),
    ]