# Generated by Django 5.0.7 on 2024-07-17 16:25

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Expense",
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
                ("description", models.CharField(max_length=255)),
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date", models.DateField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name="InventoryItem",
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
                ("name", models.CharField(max_length=100)),
                ("quantity", models.IntegerField()),
                (
                    "purchase_price",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("selling_price", models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name="Invoice",
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
                ("customer_name", models.CharField(max_length=100)),
                ("customer_email", models.EmailField(max_length=254)),
                ("invoice_date", models.DateField(auto_now_add=True)),
                ("due_date", models.DateField()),
                ("total_amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("paid", models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name="Payment",
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
                ("amount", models.DecimalField(decimal_places=2, max_digits=10)),
                ("payment_date", models.DateField(auto_now_add=True)),
                ("method", models.CharField(max_length=50)),
                (
                    "invoice",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="business.invoice",
                    ),
                ),
            ],
        ),
    ]