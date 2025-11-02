from django.db import models
from .product import Product
from .user import User


class Log(models.Model):
    log_prod_id = models.AutoField(primary_key=True)
    update_date = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=60, null=False, blank=False)
    update_description = models.TextField(null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    movement_qty = models.DecimalField(max_digits=10, decimal_places=2, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    project = models.CharField(max_length=255, null=True, blank=True)
    client = models.CharField(max_length=255, null=True, blank=True)

    class Meta:
        db_table = 'logs'
        ordering = ['-update_date']
        verbose_name = 'Log'
        indexes = [
            models.Index(fields=['update_date']),
            models.Index(fields=['type']),
            models.Index(fields=['update_description']),
            models.Index(fields=['movement_qty']),
            models.Index(fields=['client']),
            models.Index(fields=['project']),
        ]

    def __str__(self):
        return str(self.product.category)
