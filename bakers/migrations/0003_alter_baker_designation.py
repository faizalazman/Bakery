# Generated by Django 3.2.4 on 2021-06-04 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bakers', '0002_baker_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='baker',
            name='designation',
            field=models.CharField(choices=[('Founder', 'Founder'), ('Master Chef', 'Master Chef'), ('Master Baker', 'Master Baker'), ('Junior Baker', 'Junior Baker')], default='JuniorBaker', max_length=50),
        ),
    ]