from django.urls import path
from .views import SupplierListView, supplier_form
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('suppliers/', SupplierListView.as_view(), name='supplier_list'),
    path('supplier/form/', supplier_form, name='supplier_form'),

]