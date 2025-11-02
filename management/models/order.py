from django.db import models
from .supplier import Supplier


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    order_number = models.IntegerField(null=False, blank=False, unique=True)
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    code = models.CharField(max_length=60, null=False, blank=False)
    create_date = models.DateTimeField(null=False, blank=False)
    sent_date = models.DateTimeField(null=True, blank=True)
    expected_delivery_date = models.DateTimeField(null=False, blank=False)
    closing_date = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=60, null=False, blank=False)
    order_comment = models.TextField(null=True, blank=True)

    class Meta:
        db_table = 'orders'
        ordering = ['order_id']
        verbose_name = 'Order'
        indexes = [
            models.Index(fields=['code']),
            models.Index(fields=['create_date']),
            models.Index(fields=['sent_date']),
            models.Index(fields=['expected_delivery_date']),
            models.Index(fields=['closing_date']),
            models.Index(fields=['status']),
            models.Index(fields=['order_comment']),
        ]

    def __str__(self):
        return str(self.order_number)
