# Generated by Django 3.0.3 on 2020-07-29 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0020_auto_20200728_1825'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='timer',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
