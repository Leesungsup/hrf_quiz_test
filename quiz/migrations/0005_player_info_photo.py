# Generated by Django 3.2.3 on 2021-06-26 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0004_auto_20210619_2247'),
    ]

    operations = [
        migrations.AddField(
            model_name='player_info',
            name='photo',
            field=models.ImageField(default='', upload_to='photos/'),
        ),
    ]
