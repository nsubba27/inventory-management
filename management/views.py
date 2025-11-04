from django.shortcuts import render
from .models import Supplier
from django.views.generic import ListView
from .forms import SupplierForm

# Create your views here.
class SupplierListView(ListView):
    model = Supplier
    template_name = 'management/suppliers.html'
    context_object_name = 'suppliers'
    ordering = ['company_name']

def supplier_form(request):
    if request.method == 'POST':
        form = SupplierForm(request.POST)
        if form.is_valid():
            form.save()
            suppliers = Supplier.objects.all().order_by('company_name')
            return render(request, 'management/tables/supplier-table.html', {'suppliers': suppliers})
    else:
        form = SupplierForm()
    return render(request, 'management/forms/supplier-form.html', {'form': form})
def homepage(request):
    return render(request, 'homepage.html')


def dashboard(request):
    return render(request, 'partials/dashboard.html')