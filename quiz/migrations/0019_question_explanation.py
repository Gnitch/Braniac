# Generated by Django 3.0.3 on 2020-07-28 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0018_quiz_answer_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='explanation',
            field=models.TextField(default='READ YURI'),
            preserve_default=False,
        ),
    ]
