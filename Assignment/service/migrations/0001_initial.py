# Generated by Django 4.2.4 on 2023-09-25 18:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='customer_info',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer_id', models.IntegerField()),
                ('name', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=40)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
