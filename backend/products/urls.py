from django.urls import path
from .views import (
    ListCreateProductApiView,
    ProductDetailApiView,
    UpdateProductDetailApiView,
    DeleteProductDetailApiView,
)

urlpatterns = [
    path("", ListCreateProductApiView.as_view(), name="create_product"),
    path("<int:pk>/", ProductDetailApiView.as_view(), name="product_details"),
    path(
        "<int:pk>/update/",
        UpdateProductDetailApiView.as_view(),
        name="update_details",
    ),
    path(
        "<int:pk>/delete/",
        DeleteProductDetailApiView.as_view(),
        name="delete_product",
    ),
]
