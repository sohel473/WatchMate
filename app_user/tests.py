from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework.authtoken.models import Token


class RegisterTests(APITestCase):

  def test_register(self):
    url = reverse('register')
    data = {
      'username': 'testuser',
      'email': 'test@gmail.com',
      'password': 'testpassword123',
      'password_confirmation': 'testpassword123'
    }
    response = self.client.post(url, data, format='json')
    
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

class LoginLogoutTestCase(APITestCase):

    def setUp(self):
      self.user = User.objects.create_user(username="example", password="NewPassword@123")

    def test_login(self):
      url = reverse('login')
      data = {
          "username": "example",
          "password": "NewPassword@123"
      }
      response = self.client.post(url, data)
      self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_logout(self):
      self.token = Token.objects.get(user=self.user) # or get(user__username="example")
      self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)
      response = self.client.post(reverse('logout'))
      self.assertEqual(response.status_code, status.HTTP_200_OK)

    