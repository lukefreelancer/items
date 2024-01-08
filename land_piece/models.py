from django.db import models

class LandPiece(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    x_position = models.CharField(max_length=100, blank=True, default='')
    y_position = models.CharField(max_length=100, blank=True, default='')
    
    def __str__(self):
        return self.title
