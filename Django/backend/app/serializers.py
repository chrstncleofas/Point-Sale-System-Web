from rest_framework import serializers
from app.models import TableStocks

class InventorySerializer(serializers.ModelSerializer):
    class Meta:
        model=TableStocks 
        fields=(
            'ProductID',
            'ProductName',
            'Category',
            'Description',
            'Qty',
            'BuyingPrice',
            'SellingPrice',
        )
