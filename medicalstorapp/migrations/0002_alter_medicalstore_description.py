# Generated by Django 5.0.2 on 2024-03-27 04:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicalstorapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalstore',
            name='description',
            field=models.TextField(max_length=100),
        ),
    ]