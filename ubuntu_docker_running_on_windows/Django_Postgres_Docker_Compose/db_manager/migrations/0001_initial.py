# Generated by Django 4.2.11 on 2024-03-13 18:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Account",
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
                ("name", models.CharField()),
                ("suffix", models.CharField()),
                ("creation_date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="Platform",
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
                ("name", models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name="RecordType",
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
                ("type", models.CharField()),
            ],
        ),
        migrations.CreateModel(
            name="Record",
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
                ("tags", models.TextField()),
                ("filename", models.CharField()),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="db_manager.recordtype",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Post",
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
                ("annotation", models.TextField()),
                ("creation_date", models.DateTimeField(auto_now_add=True)),
                (
                    "account",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="db_manager.account",
                    ),
                ),
                (
                    "record",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="db_manager.record",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="account",
            name="platform",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="db_manager.platform"
            ),
        ),
    ]