from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from products.models import Product
from .serializers import ProductSerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [filters.SearchFilter, DjangoFilterBackend, filters.OrderingFilter]
    search_fields = ['name', 'sku']
    filterset_fields = ['price', 'sku', 'inventory_quantity']
    ordering_fields = ['last_updated']

@api_view(['POST'])
@permission_classes([AllowAny])  
def shopify_inventory_webhook(request):
    sku = request.data.get('sku')
    qty = request.data.get('inventory_quantity')
    product = get_object_or_404(Product, sku=sku)
    product.inventory_quantity = qty
    product.save(update_fields=["inventory_quantity", "last_updated"])
    return Response({'status': 'inventory updated'})
