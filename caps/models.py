from django.db import models

# Create your models here.

class Caps(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    color = models.CharField(max_length=50, null=True, blank=True)
    stock = models.IntegerField()
    brand = models.ForeignKey("brands.Brand", verbose_name=("Brand"), on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cap"
        verbose_name_plural = "Caps"
    def __str__(self):
        return self.name