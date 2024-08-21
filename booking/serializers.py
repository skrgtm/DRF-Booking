# booking/serializers.py
from rest_framework import serializers
from .models import Booking

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'property', 'booking_date', 'created_at', 'updated_at']  # Exclude 'user'
