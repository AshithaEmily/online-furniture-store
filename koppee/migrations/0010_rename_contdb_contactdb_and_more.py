# Generated by Django 4.1.3 on 2023-01-06 10:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('koppee', '0009_rename_contactdb_contdb'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contdb',
            new_name='contactdb',
        ),
        migrations.RenameField(
            model_name='coffeedb',
            old_name='Coffeename',
            new_name='furniturename',
        ),
    ]
