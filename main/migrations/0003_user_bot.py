# Generated by Django 4.1.7 on 2023-07-13 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_bot_bot_tokken'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='bot',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='main.bot'),
            preserve_default=False,
        ),
    ]
