# Generated by Django 4.2.3 on 2023-09-28 15:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainApp', '0022_buyer_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='checkout',
            name='rppid',
            field=models.CharField(default='', max_length=30),
        ),
    ]
