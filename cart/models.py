from django.db import models

# Create your models here.

class CartSession(models.Model):
    user = models.ForeignKey("users.CustomUser", on_delete=models.CASCADE)
    createdAt = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=True)

class CartItem(models.Model):
    cart = models.ForeignKey("cart.CartSession", on_delete=models.CASCADE)
    product = models.ForeignKey("caps.Caps", on_delete=models.CASCADE)
    quantity = models.IntegerField()