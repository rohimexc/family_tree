# Generated by Django 4.1.5 on 2023-01-28 02:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("family_app", "0003_family_fid_family_mid_family_pids_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="OptionCity",
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
                ("city", models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name="OptionCountry",
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
                ("country", models.CharField(max_length=50)),
            ],
        ),
        migrations.AlterField(
            model_name="optionfamily",
            name="name",
            field=models.CharField(max_length=50),
        ),
    ]