from django.test import TestCase
from django.urls import reverse, resolve
from users.models import User

from payments.models import Payment
from maintenance.models import MaintRequest, Rental

class TestViews(TestCase):

    def setUp(self):
        """ Create and login user for tests """

        self.user = User.objects.create_user(username='my_username', password='my_password')
        self.user.save()
        self.login = self.client.login(username='my_username', password='my_password')

    def test_payments_list_view(self):

        url = reverse('payments-list')

        # test GET
        get_response = self.client.get(url)

        self.assertEqual(get_response.status_code, 200)
        self.assertTemplateUsed(get_response, 'payments/payments_list.html')

        # test POST
        post_response = self.client.post(url, data = {'maint_request': 'test', 'amount': 50}, follow=True)

        self.assertEqual(post_response.status_code, 200)

    def test_payment_delete_view(self):

        payment = Payment(amount=10)
        payment.save()
        url = reverse('payments-delete', args=[payment.id])

        response = self.client.get(url)

        self.assertEqual(response.status_code, 302)