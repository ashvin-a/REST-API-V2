from django.urls import path
from .views import (ProductDetailApiView,
                    CreateProductApiView,)

urlpatterns = [
    path('',CreateProductApiView.as_view(),name='create_product'),
    path('<int:pk>/',ProductDetailApiView.as_view(),name='product_details'),
]
