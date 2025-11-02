from django.urls import path
from .views import SupplierListView
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('suppliers/', SupplierListView.as_view(), name='supplier_list')
]