# Generated by Django 4.1.5 on 2023-02-09 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("family_app", "0014_delete_optionfamily"),
    ]

    operations = [
        migrations.AlterField(
            model_name="family",
            name="pids",
            field=models.FloatField(blank=True, null=True),
        ),
    ]
