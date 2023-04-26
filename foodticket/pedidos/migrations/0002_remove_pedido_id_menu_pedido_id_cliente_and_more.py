# Generated by Django 4.1.7 on 2023-04-21 01:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("clientes", "0007_alter_cliente_id_restaurante"),
        ("menus", "0009_remove_menu_precio"),
        ("restaurantes", "0002_alter_restaurante_nit_alter_restaurante_tipo_and_more"),
        ("pedidos", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="pedido",
            name="id_menu",
        ),
        migrations.AddField(
            model_name="pedido",
            name="id_cliente",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="clientes.cliente",
            ),
        ),
        migrations.AlterField(
            model_name="pedido",
            name="id_restaurante",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="restaurantes.restauranteusuario",
            ),
        ),
        migrations.CreateModel(
            name="MenuPedido",
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
                ("cantidad", models.IntegerField(default=1)),
                (
                    "id_menu",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="menus.menu"
                    ),
                ),
                (
                    "id_pedido",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="pedidos.pedido"
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="pedido",
            name="menus_comprados",
            field=models.ManyToManyField(through="pedidos.MenuPedido", to="menus.menu"),
        ),
    ]