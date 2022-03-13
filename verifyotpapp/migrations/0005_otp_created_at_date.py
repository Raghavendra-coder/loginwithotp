# Generated by Django 4.0.3 on 2022-03-12 00:54

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('verifyotpapp', '0004_otp'),
    ]

    operations = [
        migrations.AddField(
            model_name='otp',
            name='created_at_date',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
