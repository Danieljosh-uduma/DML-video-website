# Generated by Django 5.0.6 on 2024-07-09 02:14

import django.db.models.deletion
import embed_video.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chat', '0002_initial'),
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', embed_video.fields.EmbedVideoField()),
                ('posted', models.DateTimeField(auto_now=True)),
                ('topic', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='chat.topic')),
                ('tutor', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='home.tutor')),
            ],
            options={
                'ordering': ['-posted', 'topic'],
            },
        ),
    ]