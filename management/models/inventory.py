from django.db import models
from .product import Product


class Inventory(models.Model):
    inventory_id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    expected_qty = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    actual_qty = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    qty_difference = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'inventory'
        ordering = ['inventory_id']
        verbose_name = 'Inventory'
        verbose_name_plural = 'Inventories'
        indexes = [
            models.Index(fields=['expected_qty']),
            models.Index(fields=['actual_qty']),
            models.Index(fields=['qty_difference'])
        ]

    def __str__(self):
        return str(self.inventory_id)
