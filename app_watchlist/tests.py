from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase
from rest_framework.authtoken.models import Token

from app_watchlist.api import serializers
from app_watchlist import models

class StreamPlatformTest(APITestCase):

  def setUp(self):
    self.user = User.objects.create_user(username="example", password="Password@123")
    # print(self.user)
    self.token = Token.objects.get(user=self.user)
    self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

    self.stream = models.StreamPlatform.objects.create(name="Netflix", about="#1 Platform", website="https://www.netflix.com")

  def test_streamplatform_create(self):
    data = {
        "name": "Netflix",
        "about": "#1 Streaming Platform",
        "website": "https://netflix.com"
    }
    response = self.client.post(reverse('streams-list'), data)
    self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

  def test_streamplatform_list(self):
    response = self.client.get(reverse('streams-list'))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

  def test_streamplatform_ind(self):
    response = self.client.get(reverse('streams-detail', args=(self.stream.id,)))
    self.assertEqual(response.status_code, status.HTTP_200_OK)

class WatchListTestCase(APITestCase):

    def setUp(self):
      self.user = User.objects.create_user(username="example", password="Password@123")
      self.token = Token.objects.get(user=self.user)
      self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.token.key)

      self.stream = models.StreamPlatform.objects.create(name="Netflix", about="#1 Platform", website="https://www.netflix.com")
      
      self.watchlist = models.WatchList.objects.create(platform=self.stream, title="Example Movie", storyline="Example Movie", active=True)

    def test_watchlist_create(self):
      data = {
          "platform": self.stream,
          "title": "Example Movie",
          "storyline": "Example Story",
          "active": True
      }
      response = self.client.post(reverse('movie-list'), data)
      self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_watchlist_list(self):
      response = self.client.get(reverse('movie-list'))
      self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_watchlist_ind(self):
      response = self.client.get(reverse('movie-details', args=(self.watchlist.id,)))
      self.assertEqual(response.status_code, status.HTTP_200_OK)
      self.assertEqual(models.WatchList.objects.count(), 1)
      self.assertEqual(models.WatchList.objects.get().title, 'Example Movie')