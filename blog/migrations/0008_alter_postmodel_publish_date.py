# Generated by Django 3.2.6 on 2021-08-11 06:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_postmodel_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='publish_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
