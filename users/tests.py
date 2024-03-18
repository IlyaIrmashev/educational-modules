from datetime import datetime
from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.reverse import reverse
from users.models import User
from rest_framework_simplejwt.tokens import AccessToken


class CRUDTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create(email='Test@test.com')
        self.user.set_password('test')
        self.user.save()

    def test_users_list(self):
        url = reverse('users:user-list')
        response = self.client.get(url)
        self.assertEquals(response.status_code, status.HTTP_200_OK)
        email = response.json()[0].get('email')
        self.assertEquals(self.user.email, email)

    def test_users_create(self):
        url = reverse('users:user-list')
        data = {
            'email': 'Test@testov.com',
            'password': 'test_3'
        }
        response = self.client.post(url, data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        email = response.json().get('email')
        self.assertEquals(data['email'], email)