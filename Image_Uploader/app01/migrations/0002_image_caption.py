# Generated by Django 5.0.1 on 2024-01-26 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='caption',
            field=models.CharField(default=True, max_length=10),
        ),
    ]
