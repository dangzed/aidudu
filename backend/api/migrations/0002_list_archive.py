# Generated by Django 3.2.8 on 2021-11-25 04:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='list',
            name='archive',
            field=models.BooleanField(default=False),
        ),
    ]
