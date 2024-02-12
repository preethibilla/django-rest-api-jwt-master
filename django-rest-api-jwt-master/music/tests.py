from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Inventory
from .serializers import InventorySerializer

# Define the base URL for the API
BASE_URL = '/api/v1/inventory/'

class InventoryAPITests(TestCase):
    def setUp(self):
        # Create some inventory items for testing
        Inventory.objects.create(
            SKU='SKU001',
            name='Product 1',
            category='Electronics',
            tags='gadget, tech',
            stock_status='in stock',
            available_stock=100
        )
        Inventory.objects.create(
            SKU='SKU002',
            name='Product 2',
            category='Electronics',
            tags='gadget, tech',
            stock_status='in stock',
            available_stock=150
        )
        # Create an APIClient instance to make requests
        self.client = APIClient()

    def test_list_inventory(self):
        # Test GET request to list inventory
        response = self.client.get(BASE_URL)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Ensure correct number of items returned


    def test_filter_inventory_by_stock_status(self):
        # Test GET request to filter inventory by stock status
        response = self.client.get(BASE_URL + '?stock_status=in%20stock')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Ensure correct number of items returned

    def test_filter_inventory_by_available_stock_range(self):
        # Test GET request to filter inventory by available stock range
        response = self.client.get(BASE_URL + '?stock_status=in%20stock&min_stock=120&max_stock=200')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)  # Ensure correct number of items returned
        self.assertEqual(response.data[0]['SKU'], 'SKU002')  # Ensure correct item is returned

    # Add more test cases as needed