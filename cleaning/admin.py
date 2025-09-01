# cleaning/admin.py
from django.contrib import admin
from .models import CleaningRecord, AuditLog
import json
from django.utils.safestring import mark_safe

@admin.register(CleaningRecord)
class CleaningRecordAdmin(admin.ModelAdmin):
    list_display = ('filter', 'operator', 'supervisor', 'cleaning_date', 'cleaning_status')
    list_filter = ('cleaning_status', 'cleaning_date', 'operator', 'supervisor')
    search_fields = ('filter__filter_id', 'operator__username', 'supervisor__username')
    date_hierarchy = 'cleaning_date'
    ordering = ('-cleaning_date',)

@admin.register(AuditLog)
class AuditLogAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'user', 'action', 'table_name', 'record_id', 'ip_address')
    list_filter = ('action', 'user', 'table_name', 'created_at')
    search_fields = ('user__username', 'record_id', 'ip_address')
    date_hierarchy = 'created_at'
    ordering = ('-created_at',)
    
    # Make all fields read-only to prevent modification
    readonly_fields = [f.name for f in AuditLog._meta.fields]

    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        return False