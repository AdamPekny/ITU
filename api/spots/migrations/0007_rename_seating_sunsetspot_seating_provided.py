# Generated by Django 4.1.3 on 2022-12-12 20:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0006_alter_walkspot_expected_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sunsetspot',
            old_name='seating',
            new_name='seating_provided',
        ),
    ]
