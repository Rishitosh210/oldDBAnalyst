# Generated by Django 2.1 on 2019-03-09 20:21

import django.core.files.storage
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('audtech_analytics', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='companyinfo',
            name='logo',
            field=models.ImageField(blank=True, null=True, storage=django.core.files.storage.FileSystemStorage(location='/home/indiba/audtech_env132018/audtech_project/media'), upload_to=''),
        ),
    ]