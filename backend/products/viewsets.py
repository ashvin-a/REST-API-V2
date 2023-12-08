from rest_framework.viewsets import ModelViewSet
from .models import Product
from .serializers import ProductSerializer

class ProductViewset(ModelViewSet):
    """
    The viewset for Product model.
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    """
    While using generic viewsets, you may customize it 
    with the help of mixins. In the case of get method,
    you could specify whether to list out or retrieve 
    as follows:
    
    product_list_view = ProductGenericViewSet.as_view({'get':'list'})
    product_detail_view = ProductGenericViewSet.as_view({'get':'retrieve'})
    """