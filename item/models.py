from django.db import models
from container.models import Container
class Item(models.Model):
    title = models.CharField(max_length=100, blank=True, default='')
    container = models.ForeignKey(Container, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.title
