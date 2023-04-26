# Generated by Django 4.1.7 on 2023-04-19 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("restaurantes", "0002_alter_restaurante_nit_alter_restaurante_tipo_and_more"),
        ("clientes", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Tiquetera",
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
                ("cantidad", models.IntegerField(default=0)),
                ("redimidos", models.IntegerField(default=0)),
                (
                    "id_cliente",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="clientes.cliente",
                    ),
                ),
                (
                    "id_restaurante",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="restaurantes.restaurante",
                    ),
                ),
            ],
        ),
    ]