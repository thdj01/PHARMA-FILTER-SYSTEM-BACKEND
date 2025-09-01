# cleaning/models.py
from django.db import models
from users.models import User
from filters.models import Filter

class CleaningRecord(models.Model):
    STATUS_CHOICES = (
        ('satisfactory', 'Satisfactory'),
        ('rework', 'Rework'),
        ('rejected', 'Rejected'),
    )
    filter = models.ForeignKey(Filter, on_delete=models.CASCADE)
    operator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cleaning_operator')
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='cleaning_supervisor', null=True, blank=True)
    cleaning_date = models.DateField()
    start_time = models.DateTimeField(null=True, blank=True)
    end_time = models.DateTimeField(null=True, blank=True)
    washing_start_time = models.DateTimeField(null=True, blank=True)
    washing_end_time = models.DateTimeField(null=True, blank=True)
    water_pressure = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    air_pressure = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    drying_start_time = models.DateTimeField(null=True, blank=True)
    drying_end_time = models.DateTimeField(null=True, blank=True)
    drying_temperature = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    total_drying_time = models.IntegerField(null=True, blank=True) # in minutes
    cleaning_status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='satisfactory')
    operator_signature = models.TextField(null=True, blank=True)
    supervisor_signature = models.TextField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)
    remarks = models.TextField(null=True, blank=True)

class AuditLog(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    action = models.CharField(max_length=100)
    table_name = models.CharField(max_length=50, null=True, blank=True)
    record_id = models.IntegerField(null=True, blank=True)
    old_values = models.JSONField(null=True, blank=True)
    new_values = models.JSONField(null=True, blank=True)
    ip_address = models.GenericIPAddressField(null=True, blank=True)
    user_agent = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)