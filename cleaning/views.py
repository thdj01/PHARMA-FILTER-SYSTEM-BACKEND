# cleaning/views.py
from rest_framework import viewsets
from .models import CleaningRecord, AuditLog
from .serializers import CleaningRecordSerializer, AuditLogSerializer

class CleaningRecordViewSet(viewsets.ModelViewSet):
    queryset = CleaningRecord.objects.all()
    serializer_class = CleaningRecordSerializer

class AuditLogViewSet(viewsets.ModelViewSet):
    queryset = AuditLog.objects.all()
    serializer_class = AuditLogSerializer