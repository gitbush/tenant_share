from django.test import TestCase
from users.models import User, Profile
from django.urls import reverse, resolve

from maintenance.views import Home
from maintenance.models import Rental, MaintRequest
from maintenance.forms import (MaintenanceCreationForm,
                               MaintenanceQuoteForm)


class TestViews(TestCase):

    def setUp(self):

        self.user = User.objects.create_user(username='my_username', password='my_password')
        self.user.save()
        self.rental = Rental(address='test street', no_of_tenants=2)
        self.rental.save()
        self.login = self.client.login(username='my_username', password='my_password')

    def test_home_view(self):

        url = reverse('maint-home')
        response = self.client.get(url)

        # Check user is logged in
        self.assertEqual(str(response.context['user']), 'my_username')

        # check that a rental instance is not in context 
        # if current user doesn't have a rental assigned
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('userRental', response.context)

        # test rental is in context when assigned
        self.user.profile.rental = self.rental
        self.user.profile.save()
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('userRental' in response.context)
        self.assertTemplateUsed(response, 'maintenance/home.html')

    def test_maintenance_list_view(self):

        url = reverse('maint-list')
        response = self.client.get(url)

        # test when user has no rental
        self.assertEqual(response.status_code, 200)
        self.assertNotIn('user_rental', response.context)

        # test user with rental
        self.user.profile.rental = self.rental
        self.user.profile.save()
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTrue('requests' in response.context)

    def test_maintenance_create_view(self):

        url = reverse('maint-create')

        # test POST request
        response = self.client.post(url, {'request_create_form': 'True', 'title': 'A test request', 'details': 'test request', 'priority': 'high', 'image': 'test_image.png'})
    
        req = MaintRequest.objects.filter(title='A test request')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, '/maintenance/request/1/')

        # test GET request
        response = self.client.get(url, {'request_create_form': 'True'})

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'maintenance/maint_create.html')

    def test_maintenance_detail_view(self):

        maint_request = MaintRequest(title='Detail test request', status='low')
        maint_request.save()
        url = reverse('maint-detail', args=[maint_request.id])

        # test assign cost redirect
        response = self.client.post(url, {'assign_cost_form': 'True', 'cost': 100, 'paid_by': 'Tenant'})

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('maint-detail', args=[maint_request.id]))

    def test_maintenance_delete_view(self):

        maint_request = MaintRequest(title='Detail test request')
        maint_request.save()
        url = reverse('maint-delete', args=[maint_request.id])

        # test redirect after maint request delete
        response = self.client.get(url)

        self.assertRedirects(response, reverse('maint-list'))









        





        
