# Generated by Django 4.0.1 on 2022-01-19 09:07

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('su_list', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='sulist',
            name='user',
        ),
    ]
