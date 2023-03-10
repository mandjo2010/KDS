# Generated by Django 3.1.14 on 2023-02-01 14:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cœur', '0015_auto_20230201_1408'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='category',
            options={'ordering': ['titre'], 'verbose_name': 'category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='produit',
            options={'ordering': ['titre'], 'verbose_name_plural': 'Produits'},
        ),
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(default='', upload_to='produits/%Y/%m/%d'),
        ),
        migrations.AlterField(
            model_name='produit',
            name='image_view',
            field=models.ImageField(default='', upload_to='produits/%Y/%m/%d'),
        ),
        migrations.AddIndex(
            model_name='category',
            index=models.Index(fields=['titre'], name='cœur_catego_titre_ba4502_idx'),
        ),
        migrations.AddIndex(
            model_name='produit',
            index=models.Index(fields=['id', 'slug'], name='cœur_produi_id_e724c9_idx'),
        ),
        migrations.AddIndex(
            model_name='produit',
            index=models.Index(fields=['titre'], name='cœur_produi_titre_6956d2_idx'),
        ),
        migrations.AddIndex(
            model_name='produit',
            index=models.Index(fields=['-date'], name='cœur_produi_date_3550f7_idx'),
        ),
    ]
