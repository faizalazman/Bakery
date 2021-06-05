# Generated by Django 3.2.4 on 2021-06-04 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('after_discount', models.DecimalField(blank=True, decimal_places=2, max_digits=5)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('hot_item', models.BooleanField(default=False)),
                ('added_on', models.DateField(auto_now_add=True)),
                ('photo', models.ImageField(upload_to='')),
                ('best_seller', models.BooleanField()),
            ],
        ),
    ]
