from django.urls import reverse
from django.test import TestCase

from users.models import User, Profile
from maintenance.models import Rental

class TestViews(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='my_username', password='my_password')
        self.user.save()
        self.login = self.client.login(username='my_username', password='my_password')

    def test_register_view(self):

        url = reverse('register')

        # test GET
        get_response = self.client.get(url)

        self.assertEqual(get_response.status_code, 200)

    def test_account_view(self):

        url = reverse('account', args=[self.user.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)

