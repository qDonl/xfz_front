# Generated by Django 2.1 on 2019-09-01 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='desc',
            field=models.TextField(default='暂无描述信息'),
        ),
    ]
