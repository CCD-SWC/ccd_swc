# Generated by Django 2.2.5 on 2020-02-08 13:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0005_remove_company_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='logo',
            field=models.ImageField(blank=True, upload_to='company_logo'),
        ),
        migrations.AlterField(
            model_name='hostel',
            name='image',
            field=models.ImageField(blank=True, upload_to='hostel_maps'),
        ),
    ]
