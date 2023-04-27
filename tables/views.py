from django.shortcuts import render
from django.views import generic
from .models import Table, TableEntry

# Create your views here.

class TableList(generic.ListView):
    queryset = Table.objects.order_by('name')
    template_name = 'table_list.html'

class TableDetail(generic.DetailView):
    model = Table
    template_name = 'table_detail.html'