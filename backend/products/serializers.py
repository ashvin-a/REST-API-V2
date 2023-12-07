from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    
    retail_price = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = ['id','title','content','price','retail_price',]
    
    def get_retail_price(self,obj):
        try:
            return obj.sale_price
        except:
            return None