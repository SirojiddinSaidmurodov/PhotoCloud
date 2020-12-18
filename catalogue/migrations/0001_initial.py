# Generated by Django 3.1.4 on 2020-12-18 19:43

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoMetaData',
            fields=[
                ('id', models.UUIDField(help_text='UUID is a photo name', primary_key=True, serialize=False)),
                ('placeLat', models.FloatField(help_text='Latitude of place', null=True)),
                ('placeLong', models.FloatField(help_text='Longitude of place', null=True)),
                ('placeName', models.TextField(help_text='Address of place', max_length=512, null=True)),
                ('camera', models.TextField(help_text='Camera model', max_length=255, null=True)),
                ('shootDate', models.DateTimeField(help_text='Date when photo taken')),
            ],
            options={
                'ordering': ['shootDate'],
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=20)),
                ('photo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='catalogue.photometadata')),
            ],
        ),
    ]
