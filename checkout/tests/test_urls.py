from django.test import TestCase
from django.urls import reverse, resolve

from checkout.views import checkout
from payments.models import Payment
from maintenance.models import MaintRequest, Rental

class TestUrls(TestCase):

    def test_url_is_resolved(self):
        """ test url uses correct view """

        rental = Rental(address='11 Test Street')
        maint_request = MaintRequest(property_ref=rental, title='test')

        payment = Payment(id=1, maint_request=maint_request, amount=50)
        url = reverse('checkout', args=[payment.id])

        self.assertEqual(resolve(url).func, checkout)
