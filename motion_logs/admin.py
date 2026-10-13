from django.contrib import admin
from .models import MotionLog

@admin.register(MotionLog)
class MotionLogAdmin(admin.ModelAdmin):
    list_display = ('location', 'time', 'movement_triggered', 'created_at')
    list_filter = ('location', 'movement_triggered')
    search_fields = ('location',)