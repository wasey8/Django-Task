from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from products.models import Product

class ProductAPITest(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='pass')
        self.client.login(username='testuser', password='pass')
        self.product = Product.objects.create(name='Test', sku='ABC123', price=10, inventory_quantity=100)

    def test_get_product_list(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, 200)
