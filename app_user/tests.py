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