from django.urls import path
# from .views import ListCreateSongsView, SongsDetailView, ListCreateItemsView
from .views import ListCreateItemsView
from .views import InventoryListView

urlpatterns = [
    # path('songs/', ListCreateSongsView.as_view(), name="songs-list-create"),
    # path('songs/<int:pk>/', SongsDetailView.as_view(), name="songs-detail"),
    path('items/', ListCreateItemsView.as_view(), name="items-list-create"),
    path('inventory/', InventoryListView.as_view(), name="inventory-list"),
]
