from django.db import models

class Brand(models.Model):
    title=models.CharField(max_length=150, unique=True)
    country = models.CharField(max_length=100)
    founded_year=models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.title

class Car(models.Model):
    model=models.CharField(max_length=255,  unique=True)
    year=models.PositiveIntegerField()
    transmission=models.CharField(max_length=50)
    fuel_type=models.CharField(max_length=50)
    price=models.DecimalField(max_digits=12, decimal_places=2)
    image=models.ImageField(upload_to='images/', null=True, blank=True)

    brand=models.ForeignKey(Brand, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.model} ({self.year})"
