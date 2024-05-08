# Generated by Django 5.0.4 on 2024-05-05 20:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("collection", "0004_museumobject_synced"),
    ]

    operations = [
        migrations.CreateModel(
            name="SyncLock",
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
                ("is_locked", models.BooleanField(default=False)),
                ("last_updated", models.DateTimeField(auto_now=True)),
            ],
        ),
    ]