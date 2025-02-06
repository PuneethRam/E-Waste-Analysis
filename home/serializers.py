# ewaste_app/serializers.py
from rest_framework import serializers
from .models import EwasteLocation

class EwasteLocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EwasteLocation
        fields = '__all__'