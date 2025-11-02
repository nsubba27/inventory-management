from django.contrib import admin
from .models import *

# Register your models here.
# admin.site.register(Supplier)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(Log)
admin.site.register(User)
admin.site.register(OrderItem)
admin.site.register(Inventory)


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    list_display = ('company_name', 'contact_first_name', 'contact_last_name', 'email_address', 'city', 'country')
    search_fields = ('company_name', 'contact_first_name', 'contact_last_name')
    list_filter = ('country', 'city')
    list_display_links = ('company_name',)
    ordering = ('company_name',)