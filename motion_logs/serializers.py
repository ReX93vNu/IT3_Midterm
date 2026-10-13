from rest_framework import serializers
from .models import MotionLog

class MotionLogSerializer(serializers.ModelSerializer):
    class Meta:
        model = MotionLog
        fields = ['movement_triggered', 'time', 'location']