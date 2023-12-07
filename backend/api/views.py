from products import models
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from products.serializers import ProductSerializer
# Create your views here.


@api_view(['GET','POST'])
def api_home(request, *args, **kwargs):
    '''This is how a DRF view look like'''
    data = {}
    instance = models.Product.objects.all().order_by('?').first()
    if instance:
        # data = model_to_dict(instance,fields=['id','content','price','sale_price'])
        data = ProductSerializer(instance).data
    return Response(data)