# Generated by Django 3.0.4 on 2020-05-27 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='user_id',
            field=models.IntegerField(default=''),
        ),
    ]
