# Generated by Django 2.1 on 2019-09-01 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='banner',
            name='image_url',
            field=models.URLField(),
        ),
        migrations.AlterField(
            model_name='banner',
            name='link_to',
            field=models.URLField(),
        ),
    ]