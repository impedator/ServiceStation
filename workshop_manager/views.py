from django.shortcuts import render
from clients.models import Client
from vehicles.models import Vehicle
from orders.models import Order
from inventory.models import Part

def index(request):
    clients = Client.objects.all()
    vehicles = Vehicle.objects.all()
    orders = Order.objects.all()
    parts = Part.objects.all()
    context = {
        'clients': clients,
        'vehicles': vehicles,
        'orders': orders,
        'parts': parts
    }
    return render(request, 'index.html', context)
