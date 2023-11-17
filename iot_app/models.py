from django.db import models

class LightIntensity(models.Model):
    intensity_value = models.IntegerField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Intensity: {self.intensity_value} at {self.timestamp}'



