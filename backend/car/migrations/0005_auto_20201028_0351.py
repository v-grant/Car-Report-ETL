# Generated by Django 3.0.4 on 2020-10-27 22:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('car', '0004_auto_20201028_0147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crashreport',
            name='file_attached',
            field=models.FileField(null=True, upload_to='files/', verbose_name=''),
        ),
    ]
