# Generated by Django 5.1.2 on 2024-10-10 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='parent_company',
            field=models.CharField(choices=[('Tata Steel', 'Tata Steel'), ('Hindalco Industries', 'Hindalco Industries'), ('UltraTech Cement', 'UltraTech Cement'), ('JSW Steel', 'JSW Steel'), ('Adani Logistics', 'Adani Logistics'), ('Vedanta', 'Vedanta'), ('Larsen & Toubro', 'Larsen & Toubro'), ('Reliance Industries', 'Reliance Industries'), ('Bharat Petroleum', 'Bharat Petroleum'), ('Godrej & Boyce', 'Godrej & Boyce')], max_length=50),
        ),
    ]
