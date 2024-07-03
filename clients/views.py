import json
from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Client
from .forms import ClientForm

def client_list(request):
    clients = Client.objects.all()
    return render(request, 'clients/client_list.html', {'clients': clients})

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'clients/client_detail.html', {'client': client})

def add_client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('client_list')
    else:
        form = ClientForm()
    return render(request, 'clients/add_client.html', {'form': form})

@csrf_exempt
def add_client_ajax(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        form = ClientForm(data)
        if form.is_valid():
            form.save()
            return JsonResponse({'success': True})
        else:
            return JsonResponse({'success': False, 'errors': form.errors})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})

@csrf_exempt
def delete_client_ajax(request, client_id):
    if request.method == 'DELETE':
        try:
            client = Client.objects.get(id=client_id)
            client.delete()
            return JsonResponse({'success': True})
        except Client.DoesNotExist:
            return JsonResponse({'success': False, 'error': 'Client not found'})
    return JsonResponse({'success': False, 'error': 'Invalid request method'})