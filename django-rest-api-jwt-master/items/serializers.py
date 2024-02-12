from rest_framework import serializers

# from .models import Songs
from .models import Inventory

# class SongsSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Songs
#         # fields = "__all__"
#         fields = ("title", "artist")

#     def update(self, instance, validated_data):
#         instance.title = validated_data.get("title", instance.title)
#         instance.artist = validated_data.get("artist", instance.artist)
#         instance.save()
#         return instance

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Inventory
        fields = ['SKU', 'name', 'category', 'tags', 'stock_status', 'available_stock']