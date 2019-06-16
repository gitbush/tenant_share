from django.test import SimpleTestCase
from django.urls import reverse, resolve
from users.views import register, login, logout

class TestUrls(SimpleTestCase):

    def test_register(self):
        """ Test for register url resolves to register view """
        url = reverse('register')
        self.assertEquals(resolve(url).view_name, 'register' )