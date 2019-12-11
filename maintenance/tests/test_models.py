from django.test import TestCase, Client
from django.urls import reverse

from maintenance.models import Rental, MaintRequest

class TestModels(TestCase):

    def setUp(self):
        """ Create necessary instances before tests """

        self.rental = Rental(address='11 Test Street')
        self.maint_request = MaintRequest(id=1, title='Test request', property_ref=self.rental)

    def test_rental_str(self):
        """ Test a rental string rep is address """

        self.assertEqual(str(self.rental), self.rental.address)

    def test_maint_request_str(self):
        """ Test a maintenance request string rep is id and title"""

        self.assertEqual(str(self.maint_request), f"#{self.maint_request.id}  {self.maint_request.title} ")
