# Generated by Django 4.1.3 on 2022-11-20 14:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_alter_posts_image_alter_posts_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='commentaires',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]