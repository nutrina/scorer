# Generated by Django 4.1.1 on 2022-10-01 10:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("scorer_apu", "0002_combo_combo"),
    ]

    operations = [
        migrations.CreateModel(
            name="NumInfo",
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
                    "stamp_count",
                    models.IntegerField(
                        blank=True, db_index=True, default=0, null=True
                    ),
                ),
                ("count", models.IntegerField(db_index=True, default=0)),
                (
                    "scorer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="scorer_apu.apuscorer",
                    ),
                ),
            ],
        ),
    ]