# Generated by Django 4.0.2 on 2022-02-15 14:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=200)),
                ('product_name', models.CharField(max_length=200)),
                ('type_name', models.CharField(max_length=200)),
                ('inches', models.FloatField()),
                ('screen_resoulation', models.CharField(max_length=200)),
                ('cpu', models.CharField(max_length=200)),
                ('ram', models.IntegerField()),
                ('memory', models.CharField(max_length=200)),
                ('gpu', models.CharField(max_length=200)),
                ('opsys', models.CharField(max_length=200)),
                ('weight', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
            ],
            options={
                'ordering': ('product_name',),
            },
        ),
    ]