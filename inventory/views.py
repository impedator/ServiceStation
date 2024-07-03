from django.shortcuts import render, redirect, get_object_or_404
from .models import Part
from .forms import PartForm

def part_list(request):
    parts = Part.objects.all()
    return render(request, 'inventory/part_list.html', {'orders': parts})

def part_detail(request, pk):
    part = get_object_or_404(part, pk=pk)
    return render(request, 'inventory/part_detail.html', {'order': part})

def add_part(request):
    if request.method == 'POST':
        form = PartForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('part_list')
    else:
        form = PartForm()
    return render(request, 'parts/add_part.html', {'form': form})
