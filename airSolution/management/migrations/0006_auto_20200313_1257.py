# Generated by Django 3.0.3 on 2020-03-13 16:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0005_auto_20200313_1253'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquina',
            name='install_date',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
