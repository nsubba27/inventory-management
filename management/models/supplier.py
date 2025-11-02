from django.db import models


class Supplier(models.Model):
    supplier_id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=255, null=False, blank=False)
    barcode = models.CharField(max_length=255, null=False, blank=False, unique=True)
    address = models.CharField(max_length=255, null=False, blank=False)
    zip_code = models.CharField(max_length=10, null=False, blank=False)
    city = models.CharField(max_length=100, null=False, blank=False)
    country = models.CharField(max_length=100, null=False, blank=False)
    contact_last_name = models.CharField(max_length=60, null=False, blank=False)
    contact_first_name = models.CharField(max_length=60, null=False, blank=False)
    title = models.CharField(max_length=60, null=False, blank=False)
    primary_phone_number = models.CharField(max_length=20, null=False, blank=False, unique=True)
    secondary_phone_number = models.CharField(max_length=20, null=True, blank=True)
    email_address = models.CharField(max_length=100, null=False, blank=False, unique=True)
    fax_address = models.CharField(max_length=100, null=True, blank=True, unique=True)

    class Meta:
        db_table = 'suppliers'
        ordering = ['company_name']
        verbose_name = 'Supplier'
        indexes = [
            models.Index(fields=['company_name']),
            models.Index(fields=['address']),
            models.Index(fields=['zip_code']),
            models.Index(fields=['city']),
            models.Index(fields=['country']),
            models.Index(fields=['city', 'zip_code']),
            models.Index(fields=['contact_last_name']),
            models.Index(fields=['contact_first_name']),
            models.Index(fields=['contact_first_name', 'contact_last_name']),
            models.Index(fields=['title']),
            models.Index(fields=['secondary_phone_number']),
        ]

    def __str__(self):
        return self.company_name
