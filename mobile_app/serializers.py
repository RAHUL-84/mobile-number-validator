# mobile_app/serializers.py
from rest_framework import serializers

class MobileSerializer(serializers.Serializer):
    mobile = serializers.CharField(max_length=15)
