# Generated by Django 4.1.13 on 2024-04-09 17:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kursy', '0004_course_students'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-created']},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['title']},
        ),
        migrations.AlterField(
            model_name='module',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='kursy.course'),
        ),
    ]
