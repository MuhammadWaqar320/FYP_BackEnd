# Generated by Django 3.2.6 on 2021-12-02 09:21

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=350)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('customer_id', models.AutoField(primary_key=True, serialize=False)),
                ('customer_phone', models.CharField(default='', max_length=20)),
                ('customer_password', models.CharField(default='', max_length=30)),
                ('customer_name', models.CharField(max_length=150)),
                ('customer_email', models.EmailField(default='', max_length=230)),
            ],
        ),
        migrations.CreateModel(
            name='Shipper',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shipper_name', models.CharField(max_length=150)),
                ('shipper_email', models.EmailField(max_length=100)),
                ('shipper_image', models.ImageField(upload_to='uploads/images')),
                ('shipper_phone_no', models.CharField(max_length=20)),
                ('shipper_address', models.CharField(max_length=200)),
                ('shipper_Regiter_Date', models.DateField()),
                ('shipper_verified', models.BooleanField()),
                ('shipper_detail', ckeditor.fields.RichTextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='SpecialOffer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offer_name', models.CharField(max_length=150)),
                ('offer_Finish_Time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='SubmittedReview',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Product_Name', models.CharField(default='', max_length=200)),
                ('Customer_Name', models.CharField(default='', max_length=300)),
                ('rating', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subCategory_name', models.CharField(max_length=500)),
                ('category', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fypbackendapi.category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('product_name', models.CharField(max_length=500)),
                ('product_price', models.FloatField()),
                ('product_description', ckeditor.fields.RichTextField(blank=True)),
                ('product_brand', models.CharField(max_length=500)),
                ('product_color', models.CharField(max_length=50)),
                ('product_image', models.ImageField(blank=True, null=True, upload_to='uploads/images')),
                ('product_companyName', models.CharField(max_length=500)),
                ('product_total_stock', models.IntegerField()),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fypbackendapi.category')),
                ('subCategory', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='fypbackendapi.subcategory')),
            ],
        ),
    ]
