# Generated by Django 3.0.3 on 2020-08-01 11:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0026_remove_poll_deactivate'),
    ]

    operations = [
        migrations.AddField(
            model_name='poll',
            name='show_result',
            field=models.BooleanField(default=False),
        ),
    ]
