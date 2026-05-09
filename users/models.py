from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    extra_kwargs = {
        'password': {'write_only': True}
    }

    def __str__(self):
        return self.username