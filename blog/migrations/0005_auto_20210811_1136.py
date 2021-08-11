# Generated by Django 3.2.6 on 2021-08-11 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_postmodel_content'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='publish',
            field=models.CharField(choices=[('draft', 'Draft'), ('publish', 'Publish'), ('private', 'Private')], default='draft', max_length=120),
        ),
        migrations.AlterField(
            model_name='postmodel',
            name='title',
            field=models.CharField(default='New Title', max_length=226, verbose_name='Post title'),
        ),
    ]