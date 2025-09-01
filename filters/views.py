# filters/views.py
from rest_framework import viewsets
from .models import Plant, AHU, FilterType, Filter
from .serializers import PlantSerializer, AHUSerializer, FilterTypeSerializer, FilterSerializer

class PlantViewSet(viewsets.ModelViewSet):
    queryset = Plant.objects.all()
    serializer_class = PlantSerializer

class AHUViewSet(viewsets.ModelViewSet):
    queryset = AHU.objects.all()
    serializer_class = AHUSerializer

class FilterTypeViewSet(viewsets.ModelViewSet):
    queryset = FilterType.objects.all()
    serializer_class = FilterTypeSerializer

class FilterViewSet(viewsets.ModelViewSet):
    queryset = Filter.objects.all()
    serializer_class = FilterSerializer