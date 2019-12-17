from django.test import TestCase, Client
from django.urls import reverse

from payments.models import Payment
from maintenance.models import Rental, MaintRequest
from users.models import User

class TestModels(TestCase):

    def test_payment_str(self):
        """ Test a payment string rep is maint request title """

        rental = Rental(address='Test address')
        maint_request = MaintRequest(property_ref=rental, title='test request')

        payment = Payment(maint_request=maint_request, amount=10)

        self.assertTrue(str(payment), maint_request.title)
