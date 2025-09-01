# filters/models.py
from django.db import models

class Plant(models.Model):
    name = models.CharField(max_length=100)
    location = models.CharField(max_length=200, null=True, blank=True)
    code = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name  # <-- Add this

class AHU(models.Model):
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    ahu_number = models.CharField(max_length=50)
    location = models.CharField(max_length=200)
    booth_number = models.CharField(max_length=50, null=True, blank=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.ahu_number # <-- Add this

class FilterType(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    default_cleaning_interval_days = models.IntegerField()

    def __str__(self):
        return self.name # <-- Add this

class Filter(models.Model):
    STATUS_CHOICES = (
        ('active', 'Active'),
        ('due', 'Due'),
        ('cleaning', 'Cleaning'),
        ('drying', 'Drying'),
        ('cleaned', 'Cleaned'),
        ('rejected', 'Rejected'),
    )
    filter_id = models.CharField(max_length=50, unique=True)
    ahu = models.ForeignKey(AHU, on_delete=models.CASCADE)
    filter_type = models.ForeignKey(FilterType, on_delete=models.CASCADE)
    cleaning_interval_days = models.IntegerField()
    last_cleaned_date = models.DateField(null=True, blank=True)
    next_due_date = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='active')
    qr_code_data = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.filter_id # <-- Add this