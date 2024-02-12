from django.db import models



class Inventory(models.Model):
    SKU = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=100)
    category = models.CharField(max_length=50)
    tags = models.CharField(max_length=255, blank=True)
    stock_status = models.CharField(max_length=20, blank=True)
    available_stock = models.IntegerField(default=0)

    def __str__(self):
        return self.name
