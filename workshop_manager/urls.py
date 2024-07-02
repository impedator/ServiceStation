from django.contrib import admin
from django.urls import include, path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('clients/', include('clients.urls')),
    path('vehicles/', include('vehicles.urls')),
    path('orders/', include('orders.urls')),
    path('inventory/', include('inventory.urls')),
]
