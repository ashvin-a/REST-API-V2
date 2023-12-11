from .models import Product
from rest_framework import serializers
from rest_framework.validators import UniqueValidator

def validate_title(value):
        qs = Product.objects.filter(title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f'{value} already exists!')
        return value 

unique_aano = UniqueValidator(queryset=Product.objects.all())