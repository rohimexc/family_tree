# Generated by Django 4.1.5 on 2023-01-25 03:02

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Family",
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
                ("name", models.CharField(max_length=200)),
                ("email", models.EmailField(max_length=254, null=True)),
                ("phone", models.CharField(max_length=12, null=True)),
                (
                    "gender",
                    models.CharField(
                        choices=[("male", "male"), ("female", "female")],
                        max_length=12,
                        null=True,
                    ),
                ),
                ("born", models.DateField()),
                ("country", models.CharField(max_length=200, null=True)),
                ("city", models.CharField(max_length=200, null=True)),
                (
                    "relation",
                    models.CharField(
                        choices=[
                            ("suami", "suami"),
                            ("istri", "istri"),
                            ("anak perempuan", "anak perempuan"),
                            ("anak laki-laki", "anak laki-laki"),
                            ("ayah", "ayah"),
                            ("ibu", "ibu"),
                        ],
                        max_length=200,
                        null=True,
                    ),
                ),
                ("relation_from", models.CharField(max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="OptionFamily",
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
                ("name", models.CharField(max_length=200)),
            ],
        ),
    ]