# Generated by Django 3.0 on 2021-07-15 06:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('basicbank', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transfer',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
