# Generated by Django 4.1.6 on 2023-02-28 01:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inspection', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inspectionregistration',
            old_name='registration_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='inspectionregistration',
            old_name='inspection_id',
            new_name='inspection',
        ),
        migrations.RenameField(
            model_name='inspectionregistration',
            old_name='inspector_id',
            new_name='inspector',
        ),
    ]
