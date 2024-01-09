from django.db import models
from container.models import Container
class Item(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    container = models.ForeignKey(Container, on_delete=models.CASCADE, blank=True, null=True)
    kijiji_listing = models.CharField(max_length=1000, blank=True, default='')
    facebook_listing = models.CharField(max_length=1000, blank=True, default='')

    def __str__(self):
        return self.title
