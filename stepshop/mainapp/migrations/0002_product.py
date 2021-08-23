# Generated by Django 3.2.6 on 2021-08-20 10:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=228, verbose_name='product name')),
                ('image', models.ImageField(blank='True', upload_to='product_images', verbose_name='image')),
                ('short_desc', models.CharField(max_length=228, verbose_name='short description')),
                ('description', models.TextField(blank=True, verbose_name='description')),
                ('price', models.DecimalField(decimal_places=2, default=0, max_digits=8, verbose_name='price')),
                ('quantity', models.PositiveIntegerField(default=0, verbose_name='storage_quantity')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.productcategory', verbose_name='category')),
            ],
            options={
                'verbose_name': ('product',),
                'verbose_name_plural': ('products',),
            },
        ),
    ]
