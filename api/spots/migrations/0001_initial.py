# Generated by Django 4.1.3 on 2022-12-11 19:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='BMXSpotType',
            fields=[
                ('type_name', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SkateSpotType',
            fields=[
                ('type_name', models.CharField(max_length=255, primary_key=True, serialize=False, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpotCommon',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('park_near', models.BooleanField(default=None, null=True)),
                ('park_description', models.TextField(blank=True, default=None, null=True)),
                ('created', models.DateTimeField(auto_now=True)),
                ('likes', models.ManyToManyField(blank=True, related_name='likes', to=settings.AUTH_USER_MODEL)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('reports', models.ManyToManyField(blank=True, related_name='reports', to=settings.AUTH_USER_MODEL)),
                ('seen_by', models.ManyToManyField(blank=True, related_name='seen_spots', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SpotType',
            fields=[
                ('type_name', models.CharField(max_length=255, unique=True, primary_key=True)),
                ('display_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='PicnicSpot',
            fields=[
                ('spotcommon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='spots.spotcommon')),
                ('seating_provided', models.BooleanField(default=False)),
            ],
            bases=('spots.spotcommon',),
        ),
        migrations.CreateModel(
            name='SunsetSpot',
            fields=[
                ('spotcommon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='spots.spotcommon')),
                ('seating', models.BooleanField(default=False)),
            ],
            bases=('spots.spotcommon',),
        ),
        migrations.CreateModel(
            name='WalkSpot',
            fields=[
                ('spotcommon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='spots.spotcommon')),
                ('expected_duration', models.FloatField(default=None, null=True)),
                ('path_description', models.TextField(blank=True, default=None, null=True)),
            ],
            bases=('spots.spotcommon',),
        ),
        migrations.CreateModel(
            name='SpotImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('spot', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spots.spotcommon')),
            ],
        ),
        migrations.AddField(
            model_name='spotcommon',
            name='spot_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='spots.spottype'),
        ),
        migrations.CreateModel(
            name='SkateSpot',
            fields=[
                ('spotcommon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='spots.spotcommon')),
                ('guarded', models.BooleanField(default=False)),
                ('guard_free_time', models.TimeField(blank=True, default=None, null=True)),
                ('open_alltime', models.BooleanField(default=True)),
                ('open_time', models.TimeField(blank=True, default=None, null=True)),
                ('close_time', models.TimeField(blank=True, default=None, null=True)),
                ('type', models.ManyToManyField(blank=True, related_name='skate_spots', to='spots.skatespottype')),
            ],
            bases=('spots.spotcommon',),
        ),
        migrations.CreateModel(
            name='BMXSpot',
            fields=[
                ('spotcommon_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='spots.spotcommon')),
                ('guarded', models.BooleanField(default=False)),
                ('guard_free_time', models.TimeField(blank=True, default=None, null=True)),
                ('open_alltime', models.BooleanField(default=True)),
                ('open_time', models.TimeField(blank=True, default=None, null=True)),
                ('close_time', models.TimeField(blank=True, default=None, null=True)),
                ('type', models.ManyToManyField(blank=True, related_name='bmx_spots', to='spots.bmxspottype')),
            ],
            bases=('spots.spotcommon',),
        ),
    ]
