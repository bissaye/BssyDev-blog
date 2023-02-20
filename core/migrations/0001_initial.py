# Generated by Django 4.1.3 on 2022-11-19 15:42

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Posts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('thumbnail', models.ImageField(blank=True, default='thumb.jpg', null=True, upload_to='img/thumbnail/')),
                ('image', models.ImageField(blank=True, default='post.png', null=True, upload_to='img/post/')),
                ('titre', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=300)),
                ('body', ckeditor.fields.RichTextField()),
                ('date', models.DateField(auto_now_add=True)),
                ('comments', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Suscribers',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='Commentaires',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adresse', models.EmailField(max_length=254)),
                ('commentaire', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.posts')),
            ],
        ),
    ]
