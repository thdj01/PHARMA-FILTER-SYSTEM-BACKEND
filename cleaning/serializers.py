# cleaning/serializers.py
from rest_framework import serializers
from .models import CleaningRecord, AuditLog

class CleaningRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = CleaningRecord
        fields = '__all__'

class AuditLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = AuditLog
        fields = '__all__'