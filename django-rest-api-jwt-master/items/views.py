from rest_framework import generics
from rest_framework import permissions
from rest_framework.response import Response
from rest_framework.views import status

from .decorators import validate_request_data
# from .models import Songs
from .models import Inventory

# from .serializers import SongsSerializer
from .serializers import InventorySerializer
from django.db.models import Q 

    
class ListCreateItemsView(generics.ListCreateAPIView):
    """
    GET items/
    POST items/
    """
    queryset = Inventory.objects.all()
    serializer_class = InventorySerializer
    permission_classes = (permissions.IsAuthenticated,)

    @validate_request_data
    def post(self, request, *args, **kwargs):
        an_item = Inventory.objects.create(
            SKU=request.data["SKU"],
            name=request.data["name"],
            category=request.data["category"],
            tags=request.data.get("tags", ""),
            stock_status=request.data.get("stock_status", ""),
            available_stock=request.data.get("available_stock", 0)
        )
        return Response(
            data=InventorySerializer(an_item).data,
            status=status.HTTP_201_CREATED
        )
    
class InventoryListView(generics.ListAPIView):
    """
    GET /api/v1/inventory/?stock_status=<stock_status>&min_stock=<min_stock>&max_stock=<max_stock>
    """
    serializer_class = InventorySerializer

    def get_queryset(self):
        queryset = Inventory.objects.all()
        stock_status = self.request.query_params.get('stock_status')
        min_stock = self.request.query_params.get('min_stock')
        max_stock = self.request.query_params.get('max_stock')
        
        # Check if stock_status or available_stock range is provided
        if stock_status:
            queryset = queryset.filter(stock_status=stock_status)
        if min_stock and max_stock:
            queryset = queryset.filter(available_stock__range=[int(min_stock), int(max_stock)])
        elif min_stock:
            queryset = queryset.filter(available_stock__gte=int(min_stock))
        elif max_stock:
            queryset = queryset.filter(available_stock__lte=int(max_stock))
        
        return queryset
