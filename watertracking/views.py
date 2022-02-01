from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .models import Water

def water_list(request):
    waters = Water.objects.all()
    
    return render(request, 'watertracking/home.html', {'waters': waters})

@require_http_methods(['PUT'])
def water_drunk(request, pk, drunk):
    water = Water.objects.get(pk=pk)
    water.drunk = drunk
    water.save()
    
    return render(request, 'watertracking/partials/water.html', {'water': water})
