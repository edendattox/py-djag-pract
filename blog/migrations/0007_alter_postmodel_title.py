# Generated by Django 3.2.6 on 2021-08-11 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_auto_20210811_1146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(max_length=226, unique=True, verbose_name='Post title'),
        ),
    ]
