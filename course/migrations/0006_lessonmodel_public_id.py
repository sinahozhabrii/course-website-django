# Generated by Django 5.2 on 2025-04-26 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('course', '0005_coursemodel_public_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='lessonmodel',
            name='public_id',
            field=models.CharField(blank=True, max_length=130, null=True),
        ),
    ]
