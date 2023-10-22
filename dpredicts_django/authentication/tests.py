from django.test import TestCase
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APIClient
import json

class AuthenticationTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user = User.objects.create_user(
            username='testuser',
            email='test@example.com',
            password='testpassword'
        )

    def test_check_email_existing_user(self):
        url = reverse('check-email')
        data = json.dumps({'email': 'test@example.com'})

        response = self.client.post(url, data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertTrue(response_data['exists'])
        self.assertTrue('reset_token' in response_data)

    def test_check_email_non_existing_user(self):
        url = reverse('check-email')
        data = json.dumps({'email': 'nonexistent@example.com'})

        response = self.client.post(url, data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertFalse(response_data['exists'])

    def test_user_profile_authenticated_user(self):
        url = reverse('user-profile')
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        response_data = json.loads(response.content)
        self.assertEqual(response_data['username'], self.user.username)
        self.assertEqual(response_data['email'], self.user.email)

    def test_user_profile_unauthenticated_user(self):
        url = reverse('user-profile')

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
