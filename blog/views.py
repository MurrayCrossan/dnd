from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404, render
from django.template.loader import get_template
from .models import Continent, Nation, Location, Shop, Person, Item, Ship, Organisation

# Create your views here.

class IndexList(generic.ListView):
    queryset = Continent.objects.order_by('name')
    template_name = 'index.html'

def BlogDetail(request, slug):
    pages = [Continent, Nation, Location, Person, Item, Shop, Ship, Organisation]

    for page in pages:
        if page.__name__ in request.path_info:
            obj = get_object_or_404(page, slug=slug)
            template = page.__name__+"_detail.html"
            referer = str(request.META.get('HTTP_REFERER'))
            return render(request, template, {'object':obj, 'referer': referer})

def seats(request):
    return render(request, 'seats.html')
    #return render(request, 'seats/index.html')
    #return render(request, '../seats/index.html')