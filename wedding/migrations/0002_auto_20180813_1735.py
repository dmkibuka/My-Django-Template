# Generated by Django 2.0.7 on 2018-08-13 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wedding', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='eventrsvp',
            name='event',
            field=models.CharField(choices=[('Bachelor Party', 'Bachelor Party'), ('Bachelorette Party', 'Bachelorette Party'), ('Bridal Shower', 'Bridal Shower'), ('Church Service', 'Church Service'), ('Reception', 'Reception')], default='Church Service', max_length=20),
        ),
        migrations.AlterField(
            model_name='eventrsvp',
            name='guest',
            field=models.CharField(choices=[('00', '00'), ('01', '01'), ('02', '02'), ('03', '03'), ('04', '04'), ('05', '05')], default='00', max_length=2),
        ),
    ]