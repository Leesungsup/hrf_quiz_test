# Generated by Django 3.2.3 on 2021-06-26 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0009_delete_player_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player_info',
            name='name',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='player_info',
            name='nation',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='player_info',
            name='position',
            field=models.CharField(max_length=30),
        ),
    ]
