# Generated by Django 3.2.3 on 2021-06-26 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0012_auto_20210626_2356'),
    ]

    operations = [
        migrations.AddField(
            model_name='player_info',
            name='photo',
            field=models.ImageField(blank=True, default='', null=True, upload_to='photos/'),
        ),
    ]
