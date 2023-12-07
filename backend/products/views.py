from rest_framework import generics
from .models import Product
from .serializers import ProductSerializer
# Create your views here.

class CreateProductApiView(generics.CreateAPIView):
    '''This is the api for listing product details'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

class ProductDetailApiView(generics.RetrieveAPIView):
    '''This is the api for listing product details'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'
    

    
