from rest_framework import generics
from rest_framework.response import Response
from .models import Product
from rest_framework.generics import mixins
from .serializers import ProductSerializer
# Create your views here.


class ListCreateProductApiView(generics.ListCreateAPIView):
    '''This is the api for listing product details if its a get request and creates new product if its a post request'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)


class ProductDetailApiView(generics.RetrieveAPIView):
    '''This is the api for listing product details'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


class UpdateProductDetailApiView(generics.UpdateAPIView):
    '''This is the api for listing product details'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if instance.content is None:
            instance.content = instance.title



class DeleteProductDetailApiView(generics.DestroyAPIView):
    '''This is the api for listing product details'''
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        return super().perform_destroy(instance)

class AviyalApiView(generics.GenericAPIView,
                    mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,):
    '''This is the ultimate aviyal api view'''
    allowed_methods = ['GET', 'POST', 'PUT', 'DELETE']
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def get(self,request,*args, **kwargs):
        pk = kwargs.get('pk')
        if pk is not None:
            return self.retrieve(request,*args, **kwargs)
        return self.list(request,*args, **kwargs)

    def post(self,request,*args, **kwargs):
        return self.create(request,*args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request,*args, **kwargs)

    def delete(self, request,*args, **kwargs):
        return self.destroy(self, request,*args, **kwargs)