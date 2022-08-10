# Generated by Django 4.1 on 2022-08-10 07:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Attributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('attribute_name', models.CharField(max_length=100)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Brands',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand_name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=100)),
                ('icon', models.ImageField(upload_to='')),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Colours',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('colour_name', models.CharField(max_length=50)),
                ('colour_code', models.CharField(max_length=50)),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='gallery')),
            ],
        ),
        migrations.CreateModel(
            name='ServiceCharge',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_name', models.CharField(max_length=100)),
                ('service_type', models.CharField(choices=[('PER', 'Percentage'), ('MON', 'Money')], default='Money', max_length=50)),
                ('rate', models.IntegerField()),
                ('status', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='SubAttributes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.BooleanField(default=False)),
                ('subattribute_name', models.ManyToManyField(to='product.attributes')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField()),
                ('barcode', models.CharField(max_length=100)),
                ('thumbnail', models.ImageField(upload_to='')),
                ('description', models.TextField()),
                ('attribute_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.attributes')),
                ('brand_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.brands')),
                ('category_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.categories')),
                ('colour_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.colours')),
            ],
        ),
    ]