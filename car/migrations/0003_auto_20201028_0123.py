# Generated by Django 3.0.4 on 2020-10-27 19:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0002_requestreport'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestreport',
            name='request_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
