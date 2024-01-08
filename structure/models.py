from django.db import models
from land_piece.models import LandPiece

class Structure(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    x_position = models.CharField(max_length=100, blank=True, default='')
    y_position = models.CharField(max_length=100, blank=True, default='')
    land_piece = models.ForeignKey(LandPiece, on_delete=models.CASCADE, blank=True, null=True)
    def __str__(self):
        return self.title
