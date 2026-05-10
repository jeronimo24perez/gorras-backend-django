from django.db import models

# Create your models here.

class Caps(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.IntegerField()
    color = models.CharField(max_length=50, null=True, blank=True)
    image = models.URLField(max_length=200, null=True, blank=True)
    stock = models.IntegerField()
    brand = models.ForeignKey("brands.Brand", verbose_name=("Brand"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cap"
        verbose_name_plural = "Caps"
    def __str__(self):
        return self.name