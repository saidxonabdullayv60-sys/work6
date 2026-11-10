from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    """GET  /api/products/  -> hamma mahsulotlar
    POST /api/products/  -> yangi mahsulot yaratish
    """
    queryset = Product.objects.all().order_by('id')
    serializer_class = ProductSerializer


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    """GET / PUT / PATCH / DELETE  /api/products/<id>/"""
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
