from django.shortcuts import render, get_object_or_404
from .models import Part

def part_list(request):
    parts = Part.objects.all()
    return render(request, 'inventory/part_list.html', {'orders': parts})

def part_detail(request, pk):
    part = get_object_or_404(part, pk=pk)
    return render(request, 'inventory/part_detail.html', {'order': part})
