# Generated by Django 3.2.25 on 2024-04-10 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20240410_1544'),
    ]

    operations = [
        migrations.AddField(
            model_name='tablestocks',
            name='DateTime',
            field=models.DateTimeField(default='', verbose_name='Date and Time'),
        ),
    ]
