from rest_framework import serializers
from .models import Listing, Booking, Review

class Booking(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class Listing(serializers.ModelSerializer):
    bookings = Booking(many=True, read_only=True)

    class Meta:
        model = Listing
        fields = '__all__'
