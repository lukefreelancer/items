from django.db import models
from structure.models import Structure
class Container(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    x_position = models.CharField(max_length=100, blank=True, default='')
    y_position = models.CharField(max_length=100, blank=True, default='')
    structure = models.ForeignKey(Structure, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.title
