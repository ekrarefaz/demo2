# Generated by Django 4.1.6 on 2023-02-28 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_alter_identity_file'),
    ]

    operations = [
        migrations.AlterField(
            model_name='identity',
            name='file',
            field=models.FileField(null=True, upload_to='files/identity/'),
        ),
    ]