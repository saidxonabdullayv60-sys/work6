from decimal import Decimal

from rest_framework import status
from rest_framework.test import APITestCase

from .models import Product


class ProductAPITests(APITestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Olma', price=Decimal('12000.00'), description='Yangi olma'
        )

    def test_list_products(self):
        response = self.client.get('/api/products/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.json()), 1)
        self.assertEqual(response.json()[0]['name'], 'Olma')

    def test_create_product(self):
        data = {'name': 'Nok', 'price': '15000.50', 'description': 'Shirin'}
        response = self.client.post('/api/products/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_create_product_without_name_fails(self):
        response = self.client.post('/api/products/', {'price': '100'}, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('name', response.json())

    def test_create_product_negative_price_fails(self):
        data = {'name': 'Xato', 'price': '-5'}
        response = self.client.post('/api/products/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('price', response.json())

    def test_retrieve_product(self):
        response = self.client.get(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.json()['name'], 'Olma')

    def test_update_product(self):
        response = self.client.patch(
            f'/api/products/{self.product.id}/', {'price': '13000'}, format='json'
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.product.refresh_from_db()
        self.assertEqual(self.product.price, Decimal('13000.00'))

    def test_delete_product(self):
        response = self.client.delete(f'/api/products/{self.product.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

    def test_retrieve_missing_returns_404(self):
        response = self.client.get('/api/products/9999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
