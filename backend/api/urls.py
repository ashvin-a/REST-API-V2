from django.urls import path,include
from rest_framework.authtoken.views import obtain_auth_token
from . import views
from cfehome import routers

urlpatterns = [
    path('',views.api_home), # localhost:3000/api/
    path('products/',include('products.urls')), # localhost:3000/api/products/
    path('auth/',obtain_auth_token),
    path('v2/',include('cfehome.routers'))
]
