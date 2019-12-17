from django.test import TestCase

from payments.forms import PaymentForm
from maintenance.models import MaintRequest, Rental

class TestForms(TestCase):

    def test_payment_form_valid_data(self):
        """ Test form with valid data """
        rental = Rental(address='Test address')
        maint_request = MaintRequest(property_ref=rental, title='test request')
        form = PaymentForm(property_ref=rental, data={
            'maint_request': maint_request,
            'amount': '10'})

        self.assertTrue(form.is_valid)



