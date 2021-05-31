# Generated by Django 3.1.7 on 2021-05-06 16:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('races', '0001_initial'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='driverposition',
            unique_together=None,
        ),
        migrations.RemoveField(
            model_name='driverposition',
            name='driver',
        ),
        migrations.RemoveField(
            model_name='driverposition',
            name='race',
        ),
        migrations.DeleteModel(
            name='Driver',
        ),
        migrations.DeleteModel(
            name='DriverPosition',
        ),
        migrations.DeleteModel(
            name='Race',
        ),
    ]
