from rest_framework import serializers


from .models import Inventory



class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['SKU', 'name', 'category', 'tags', 'stock_status', 'available_stock']