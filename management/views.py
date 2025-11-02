from django.shortcuts import render
from .models import Supplier
from django.views.generic import ListView


# Create your views here.
class SupplierListView(ListView):
    model = Supplier
    template_name = 'management/suppliers.html'
    context_object_name = 'suppliers'
    ordering = ['company_name']


def homepage(request):
    return render(request, 'homepage.html')
