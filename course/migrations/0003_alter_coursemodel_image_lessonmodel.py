# Generated by Django 5.2 on 2025-04-24 19:11

import cloudinary.models
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0002_alter_coursemodel_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coursemodel',
            name='image',
            field=cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image'),
        ),
        migrations.CreateModel(
            name='lessonModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=120)),
                ('description', models.TextField()),
                ('image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='image')),
                ('video', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True, verbose_name='video')),
                ('can_preview', models.BooleanField(default=False, help_text='if user do not have access to course can they see this?')),
                ('status', models.CharField(choices=[('publish', 'published'), ('soon', 'coming soon'), ('draft', 'Draft')], default='draft', max_length=7)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='course.coursemodel')),
            ],
        ),
    ]
