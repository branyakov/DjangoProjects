# Generated by Django 4.1.2 on 2022-10-16 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('theblog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title_tag',
            field=models.CharField(default='My Blog', max_length=255),
        ),
    ]