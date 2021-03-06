# Generated by Django 3.1.2 on 2020-10-30 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0011_auto_20201030_1209'),
    ]

    operations = [
        migrations.AddField(
            model_name='requestreport',
            name='report_confirmation_num',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='requestreport',
            name='report_name',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='requestreport',
            name='search_result',
            field=models.CharField(blank=True, max_length=1, null=True),
        ),
    ]
