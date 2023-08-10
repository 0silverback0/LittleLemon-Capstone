from django.test import TestCase
from Restaurant.models import Menu
from rest_framework.test import APIClient
from rest_framework import status
from Restaurant.serializers import MenuSerializer
from django.contrib.auth.models import User

#TestCase class
class MenuItemTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(title="IceCream", price=80, inventory=100)
        self.assertEqual(item.get_item(), "IceCream : 80")

from django.urls import reverse

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.force_authenticate(user=self.user)
        self.menu1 = Menu.objects.create(title='Burger', price=10.99, inventory=50)
        self.menu2 = Menu.objects.create(title='Pizza', price=12.99, inventory=30)

    def test_getall(self):
        url = reverse('menu-items')
        response = self.client.get(url)
        menus = Menu.objects.all()
        serializer = MenuSerializer(menus, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)