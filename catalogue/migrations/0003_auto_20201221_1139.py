# Generated by Django 3.1.4 on 2020-12-21 08:39

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('catalogue', '0002_auto_20201221_1022'),
    ]

    operations = [
        migrations.AddField(
            model_name='photometadata',
            name='photo',
            field=models.ImageField(null=True, upload_to='<django.db.models.fields.related.ForeignKey>'),
        ),
        migrations.AlterField(
            model_name='photometadata',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
