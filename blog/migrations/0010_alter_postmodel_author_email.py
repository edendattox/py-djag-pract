# Generated by Django 3.2.6 on 2021-08-11 07:08

import blog.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_postmodel_author_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postmodel',
            name='author_email',
            field=models.CharField(blank=True, max_length=240, null=True, validators=[blog.models.validate_author_email]),
        ),
    ]
