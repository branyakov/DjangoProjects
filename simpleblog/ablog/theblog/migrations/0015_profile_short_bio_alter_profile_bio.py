# Generated by Django 4.1.4 on 2022-12-18 01:57

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0014_contact'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='short_bio',
            field=models.CharField(default='This is short bio', max_length=255),
        ),
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
