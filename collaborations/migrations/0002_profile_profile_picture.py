# Generated by Django 5.0.3 on 2024-03-07 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborations', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='profile_pics/'),
        ),
    ]