# Generated by Django 4.1.6 on 2023-02-20 07:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('landlord', '0007_property_airconditioning_property_gym_property_pool'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyInspection',
            fields=[
                ('inspection_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('date_time', models.DateTimeField(auto_now_add=True)),
                ('property_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord.property')),
            ],
        ),
        migrations.CreateModel(
            name='InspectionRegistration',
            fields=[
                ('registration_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('registered_on', models.DateTimeField(auto_now_add=True)),
                ('inspection_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='landlord.propertyinspection')),
                ('inspector_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]