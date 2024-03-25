from rest_framework import status
from rest_framework.test import APITestCase

from users.models import User


class UserTestCase(APITestCase):
    """Тестирование представления пользователя"""

    def create_user(self):
        """Создание и авторизация пользователя"""
        self.email = 'example@test.ru'
        self.user = User(email=self.email, is_staff=True)
        self.user.set_password('123Qaz')
        self.user.save()
        response = self.client.post(
            '/users/token/',
            {
                'email': self.email,
                'password': '123Qaz'
            }
        )
        self.access_token = response.json().get('access')
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.access_token}')

    def test_get_users(self):
        """Тестирование просмотра пользователей"""
        self.create_user()
        response = self.client.get('/users/', )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            [{'email': 'example@test.ru',
              'name': None}]
        )

    def test_retrieve_user(self):
        """Тестирование просмотра одного пользователя"""
        self.create_user()
        response = self.client.get(f'/users/{self.user.pk}/', )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'email': 'example@test.ru',
             'name': None
             }
        )

    def test_update_user(self):
        """Тестирование обновления пользователя"""
        self.create_user()
        response = self.client.patch(f'/users/update/{self.user.id}/', {'email': 'newexample@sky.pro',
                                                                        'name': 'test'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(
            response.json(),
            {'email': 'newexample@sky.pro',
             'name': 'test'}
        )

    def test_delete_user(self):
        """Тестирование удаления пользователя"""
        self.create_user()
        response = self.client.delete(f'/users/delete/{self.user.pk}/', )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
