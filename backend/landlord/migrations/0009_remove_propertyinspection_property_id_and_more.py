# Generated by Django 4.1.6 on 2023-02-20 08:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('landlord', '0008_propertyinspection_inspectionregistration'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='propertyinspection',
            name='property_id',
        ),
        migrations.DeleteModel(
            name='InspectionRegistration',
        ),
        migrations.DeleteModel(
            name='PropertyInspection',
        ),
    ]
