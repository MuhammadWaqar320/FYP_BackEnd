# Generated by Django 3.2.6 on 2021-10-31 11:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('fypbackendapi', '0015_rename_category_id_product_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_image',
        ),
        migrations.CreateModel(
            name='ProductImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_name', models.ImageField(upload_to='uploads/images')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fypbackendapi.category')),
            ],
        ),
    ]
