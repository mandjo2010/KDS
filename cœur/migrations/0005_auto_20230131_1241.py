# Generated by Django 3.1.14 on 2023-01-31 12:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cœur', '0004_auto_20230130_1629'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produit',
            name='collection',
        ),
        migrations.AddField(
            model_name='category',
            name='collection',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='cœur.collection'),
        ),
    ]
