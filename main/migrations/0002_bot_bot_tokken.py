# Generated by Django 4.1.7 on 2023-07-13 03:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='bot',
            name='bot_tokken',
            field=models.CharField(default=1, max_length=1000, unique=True),
            preserve_default=False,
        ),
    ]
