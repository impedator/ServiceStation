from django.urls import path
from . import views

urlpatterns = [
    path('', views.client_list, name='client_list'),
    path('add/', views.add_client, name='add_client'),
    path('add/ajax/', views.add_client_ajax, name='add_client_ajax'),
    path('delete/<int:client_id>/', views.delete_client_ajax, name='delete_client_ajax'),
    path('<int:pk>/', views.client_detail, name='client_detail'),
]
