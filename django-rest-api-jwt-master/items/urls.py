from django.urls import path
from .views import ListCreateItemsView
from .views import InventoryListView

urlpatterns = [
    path('items/', ListCreateItemsView.as_view(), name="items-list-create"),
    path('inventory/', InventoryListView.as_view(), name="inventory-list"),
]
