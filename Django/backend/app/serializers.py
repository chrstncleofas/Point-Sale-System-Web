from rest_framework import serializers
from app.models import TableStocks, TableInventory

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TableInventory
        fields = ['ProductID', 'ProductName', 'Category', 'Description', 'Qty', 'BuyingPrice', 'SellingPrice', 'Image']


