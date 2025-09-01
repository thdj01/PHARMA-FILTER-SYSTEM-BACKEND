# filters/admin.py
from django.contrib import admin
from .models import Plant, AHU, FilterType, Filter

@admin.register(Plant)
class PlantAdmin(admin.ModelAdmin):
    list_display = ('name', 'code', 'location')
    search_fields = ('name', 'code')

@admin.register(AHU)
class AHUAdmin(admin.ModelAdmin):
    # Now we can directly use 'plant' because the Plant model has a __str__ method.
    list_display = ('ahu_number', 'plant', 'location', 'booth_number', 'is_active')
    list_filter = ('plant', 'is_active')
    search_fields = ('ahu_number', 'location', 'booth_number', 'plant__name')
    list_select_related = ('plant',)

@admin.register(FilterType)
class FilterTypeAdmin(admin.ModelAdmin):
    list_display = ('name', 'default_cleaning_interval_days')
    search_fields = ('name',)

@admin.register(Filter)
class FilterAdmin(admin.ModelAdmin):
    # 'ahu' and 'filter_type' now display correctly.
    list_display = ('filter_id', 'ahu', 'filter_type', 'status', 'next_due_date')
    list_filter = ('status', 'filter_type', 'ahu__plant')
    search_fields = ('filter_id', 'ahu__ahu_number', 'ahu__plant__name')
    date_hierarchy = 'next_due_date'
    ordering = ('next_due_date',)
    list_select_related = ('ahu', 'ahu__plant', 'filter_type')