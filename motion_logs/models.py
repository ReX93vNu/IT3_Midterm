from django.db import models

class MotionLog(models.Model):
    movement_triggered = models.BooleanField(default=True)
    time = models.DateTimeField()
    location = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.location} - {self.time}"