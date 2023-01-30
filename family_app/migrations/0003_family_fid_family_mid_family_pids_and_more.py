# Generated by Django 4.1.5 on 2023-01-28 01:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("family_app", "0002_alter_family_gender_alter_family_relation_from"),
    ]

    operations = [
        migrations.AddField(
            model_name="family", name="fid", field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="family", name="mid", field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name="family", name="pids", field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name="family",
            name="gender",
            field=models.CharField(
                choices=[("male", "Laki-laki"), ("female", "Perempuan")],
                max_length=12,
                null=True,
            ),
        ),
    ]
