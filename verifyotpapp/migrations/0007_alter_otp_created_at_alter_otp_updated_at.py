# Generated by Django 4.0.3 on 2022-03-12 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('verifyotpapp', '0006_otp_failed'),
    ]

    operations = [
        migrations.AlterField(
            model_name='otp',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='otp',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
