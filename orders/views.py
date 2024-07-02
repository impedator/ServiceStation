from django.shortcuts import render, get_object_or_404
from .models import Order

def order_list(request):
    orders = Order.objects.all()
    return render(request, 'orders/order_list.html', {'orders': orders})

def order_detail(request, pk):
    order = get_object_or_404(order, pk=pk)
    return render(request, 'orders/order_detail.html', {'order': order})
