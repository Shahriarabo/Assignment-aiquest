# Generated by Django 4.2.6 on 2023-10-18 07:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('division', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Khulna', 'Khulna'), ('Sylhet', 'Sylhet'), ('Rangpur', 'Rangpur'), ('Rajshahi', 'Rajshahi'), ('Barishal', 'Barishal'), ('Chattogram', 'Chattogram'), ('Mymendhing', 'Mymendhing')], max_length=50)),
                ('district', models.CharField(max_length=200)),
                ('thana', models.CharField(max_length=50)),
                ('villprroad', models.CharField(max_length=50)),
                ('zipcode', models.IntegerField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('selling_price', models.FloatField()),
                ('discounted_price', models.FloatField()),
                ('descrition', models.TextField()),
                ('brand', models.CharField(max_length=100)),
                ('category', models.CharField(choices=[('L', 'Lehenga'), ('S', 'Seree'), ('GP', 'Gents Pant'), ('BK', 'Borkha'), ('BF', 'Baby Fashion')], max_length=2)),
                ('product_image', models.ImageField(upload_to='productimg')),
            ],
        ),
        migrations.CreateModel(
            name='OrderPlaced',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('ordered_date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Accepted', 'Accepted'), ('Packed', 'Packed'), ('On The Way', 'On The Way'), ('Delivered', 'Delivered'), ('Cancel', 'Cancel')], default='Pending', max_length=20)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.customer')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quntity', models.PositiveIntegerField(default=1)),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='info.product')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
