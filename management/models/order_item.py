from django.db import models
from .order import Order
from .product import Product


class OrderItem(models.Model):
    order_item_id = models.AutoField(primary_key=True)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    unit = models.CharField(max_length=30, null=False, blank=False)
    qty = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unit_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    class Meta:
        db_table = 'order_items'
        ordering = ['order_item_id']
        verbose_name = 'Order Item'
        indexes = [
            models.Index(fields=['unit']),
            models.Index(fields=['qty']),
            models.Index(fields=['unit_cost']),
            models.Index(fields=['total_cost'])
        ]

    def __str__(self):
        return str(self.order_item_id)
