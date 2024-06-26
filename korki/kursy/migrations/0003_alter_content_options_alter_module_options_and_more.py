# Generated by Django 4.1.13 on 2024-04-06 09:04

from django.db import migrations
import kursy.fields


class Migration(migrations.Migration):

    dependencies = [
        ('kursy', '0002_video_text_image_file_content'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='content',
            options={'ordering': ['order']},
        ),
        migrations.AlterModelOptions(
            name='module',
            options={'ordering': ['order']},
        ),
        migrations.AddField(
            model_name='content',
            name='order',
            field=kursy.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='module',
            name='order',
            field=kursy.fields.OrderField(blank=True, default=0),
            preserve_default=False,
        ),
    ]
