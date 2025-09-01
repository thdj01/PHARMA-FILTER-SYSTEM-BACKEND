# filters/serializers.py
from rest_framework import serializers
from .models import Plant, AHU, FilterType, Filter

class PlantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plant
        fields = '__all__'

class AHUSerializer(serializers.ModelSerializer):
    class Meta:
        model = AHU
        fields = '__all__'

class FilterTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FilterType
        fields = '__all__'

class FilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filter
        fields = '__all__'