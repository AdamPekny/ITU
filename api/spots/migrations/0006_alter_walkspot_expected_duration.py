# Generated by Django 4.1.3 on 2022-12-12 20:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spots', '0005_rename_guard_free_time_bmxspot_guard_free_from_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='walkspot',
            name='expected_duration',
            field=models.FloatField(blank=True, default=None, null=True),
        ),
    ]
