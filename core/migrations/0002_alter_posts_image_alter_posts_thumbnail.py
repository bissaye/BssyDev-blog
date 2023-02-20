# Generated by Django 4.1.3 on 2022-11-19 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='image',
            field=models.ImageField(blank=True, default='img/post/post.png', null=True, upload_to='img/post/'),
        ),
        migrations.AlterField(
            model_name='posts',
            name='thumbnail',
            field=models.ImageField(blank=True, default='img/thumbnail/thumb.jpg', null=True, upload_to='img/thumbnail/'),
        ),
    ]
