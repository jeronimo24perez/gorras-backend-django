from django.db import models

# Create your models here.

class Brand(models.Model):
    name = models.CharField(max_length=100)
    image = models.URLField(max_length=200, null=True, blank=True)

    def __str__(self):
        return self.name