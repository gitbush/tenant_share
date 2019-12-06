from django.test import TestCase
from django.urls import reverse, resolve

from maintenance.models import MaintRequest, Rental

from maintenance.views import (Home, 
                               MaintRequestList, 
                               MaintRequestDetail, 
                               MaintRequestCreate, 
                               MaintRequestDelete)

class TestUrls(TestCase):
    """ Test all urls resolve to correct view function """

    def setUp(self):
        self.maint_request = MaintRequest(id=1)

    def test_home_url(self):
        url = reverse('maint-home')
        self.assertEqual(resolve(url).func, Home)

    def test_list_url(self):
        url = reverse('maint-list')
        self.assertEqual(resolve(url).func, MaintRequestList)

    def test_detail_url(self):
        url = reverse('maint-detail', args=[self.maint_request.id])
        self.assertEqual(resolve(url).func, MaintRequestDetail)

    def test_create_url(self):
        url = reverse('maint-create')
        self.assertEqual(resolve(url).func, MaintRequestCreate)

    def test_delete_url(self):
        url = reverse('maint-delete', args=[self.maint_request.id])
        self.assertEqual(resolve(url).func, MaintRequestDelete)