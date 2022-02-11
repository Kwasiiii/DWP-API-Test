from django.db import models

# Create your models here.
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50, unique=True)
    ip_address = models.CharField(max_length=50)
    latitude = models.FloatField(max_length=50)
    longitude = models.FloatField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name} {self.last_name}"