from django.db import models
from .supplier import Supplier


class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    category = models.CharField(max_length=255, null=False, blank=False)
    reference = models.CharField(max_length=255, null=False, blank=False, unique=True)
    description = models.TextField(null=True, blank=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    qty = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    min_qty = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    max_qty = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    location = models.CharField(max_length=255, null=False, blank=False)
    unit_buy = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_buy = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unit_sell = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_sell = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'products'
        ordering = ['product_id']
        verbose_name = 'Product'
        indexes = [
            models.Index(fields=['category']),
            models.Index(fields=['description']),
            models.Index(fields=['location']),
            models.Index(fields=['qty']),
            models.Index(fields=['min_qty']),
            models.Index(fields=['max_qty']),
            models.Index(fields=['unit_buy']),
            models.Index(fields=['total_buy']),
            models.Index(fields=['unit_sell']),
            models.Index(fields=['total_sell']),
        ]

    def check_understock(self):
        return self.qty < self.min_qty

    def check_overstock(self):
        return self.qty > self.max_qty

    def __str__(self):
        return self.description
