# Generated by Django 3.1.14 on 2023-02-03 15:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='paid',
            new_name='payé',
        ),
    ]