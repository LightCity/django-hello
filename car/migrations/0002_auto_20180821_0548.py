# Generated by Django 2.1 on 2018-08-21 05:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='car',
            old_name='saleDate',
            new_name='sale_date',
        ),
    ]
