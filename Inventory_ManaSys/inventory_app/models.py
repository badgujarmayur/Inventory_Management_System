from django.db import models

# Create your models here.

CHOICES = [
    ('Tata Steel', 'Tata Steel'),
    ('Hindalco Industries', 'Hindalco Industries'),
    ('UltraTech Cement', 'UltraTech Cement'),
    ('JSW Steel', 'JSW Steel'),
    ('Adani Logistics', 'Adani Logistics'),
    ('Vedanta', 'Vedanta'),
    ('Larsen & Toubro', 'Larsen & Toubro'),
    ('Reliance Industries', 'Reliance Industries'),
    ('Bharat Petroleum', 'Bharat Petroleum'),
    ('Godrej & Boyce', 'Godrej & Boyce'),
]


class Inventory(models.Model):
    material = models.CharField(max_length=50)
    price = models.PositiveIntegerField()
    city = models.CharField(max_length=50)
    parent_company = models.CharField(max_length=50,choices=CHOICES)


    def __str__(self):
        return self.material