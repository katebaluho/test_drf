# Generated by Django 4.1.3 on 2022-11-08 20:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drf', '0002_profile_delete_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='account',
            field=models.FloatField(null=True, verbose_name='Счёт'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='inn',
            field=models.IntegerField(null=True, verbose_name='ИНН'),
        ),
    ]
