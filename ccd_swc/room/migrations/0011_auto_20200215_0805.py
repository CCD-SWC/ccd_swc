# Generated by Django 2.2.5 on 2020-02-15 08:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('room', '0010_merge_20200213_1848'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='company',
            name='logo',
        ),
        migrations.RemoveField(
            model_name='hostel',
            name='image',
        ),
    ]
