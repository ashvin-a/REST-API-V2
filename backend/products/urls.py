from django.urls import path
from .views import (AviyalApiView)

urlpatterns = [
    path('',AviyalApiView.as_view(),name='create_product'),
    path('<int:pk>/',AviyalApiView.as_view(),name='product_details'),
    path('<int:pk>/update/',AviyalApiView.as_view(),name='product_details'),
    path('<int:pk>/delete/',AviyalApiView.as_view(),name='product_details'),
]
