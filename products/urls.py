from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, shopify_inventory_webhook
from django.urls import path

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = router.urls + [
    path('webhook/inventory/', shopify_inventory_webhook, name='inventory-webhook'),
]
