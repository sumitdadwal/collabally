# Generated by Django 5.0.3 on 2024-03-07 10:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborations', '0002_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='is_looking_for_collaborator',
            field=models.BooleanField(default=False),
        ),
    ]