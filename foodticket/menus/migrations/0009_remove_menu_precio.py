# Generated by Django 4.1.7 on 2023-04-20 22:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("menus", "0008_remove_menu_dia1_remove_menu_dia2_remove_menu_dia3_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="menu",
            name="precio",
        ),
    ]
