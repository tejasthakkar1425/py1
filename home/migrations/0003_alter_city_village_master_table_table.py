# Generated by Django 4.2.3 on 2024-01-17 14:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_city_village_master_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='city_village_master_table',
            table='city_village_master',
        ),
    ]