# Generated by Django 5.0.7 on 2024-07-23 00:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("admin_panel", "0003_expense"),
    ]

    operations = [
        migrations.CreateModel(
            name="GSTInvoice",
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
                ("gst_number", models.CharField(max_length=15)),
                ("gst_rate", models.DecimalField(decimal_places=2, max_digits=5)),
                ("gst_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                (
                    "invoice",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="admin_panel.invoice",
                    ),
                ),
            ],
        ),
    ]