# Generated by Django 4.2.14 on 2024-08-07 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0005_booking_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='user',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
