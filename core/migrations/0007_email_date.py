# Generated by Django 4.1.3 on 2023-02-19 01:48

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_email'),
    ]

    operations = [
        migrations.AddField(
            model_name='email',
            name='date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
