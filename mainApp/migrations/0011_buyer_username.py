# Generated by Django 4.2.3 on 2023-09-10 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0010_buyer'),
    ]

    operations = [
        migrations.AddField(
            model_name='buyer',
            name='username',
            field=models.CharField(default='', max_length=30),
        ),
    ]
