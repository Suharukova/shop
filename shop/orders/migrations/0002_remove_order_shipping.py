# Generated by Django 2.2.1 on 2019-05-11 13:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='shipping',
        ),
    ]
