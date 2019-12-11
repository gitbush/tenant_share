from django.test import TestCase

from maintenance.forms import (RentalCreationForm,
                               MaintenanceCreationForm,
                               StatusUpdateForm,
                               MaintenanceQuoteForm)

class Testforms(TestCase):

    def test_rental_creation_form_valid_data(self):
        """ Test form is valid with correct data """

        form = RentalCreationForm({
            'address': '11 test st',
            'postcode': 'TESTT',
            'city': 'Test city',
            'no_of_tenants': 2,
            'image': 'test_image.png'
        })

        self.assertTrue(form.is_valid())

    def test_rental_creation_form_invalid_data(self):
        """ 
        Test form is valid with correct data 
        Test correct number of errors for required fields
        """

        form = RentalCreationForm({})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 4)

    def test_maintenance_creation_form_valid_data(self):
        """ Test form is valid with correct data """

        form = MaintenanceCreationForm({
            'title': 'A test request',
            'details': 'test request',
            'priority': 'high',
            'image': 'test_image.png'
        })

        self.assertTrue(form.is_valid())
    
    def test_maintenance_creation_form_invalid_data(self):
        """ 
        Test form is valid with missing data 
        Test correct number of errors for required fields
        """

        form = MaintenanceCreationForm({})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors), 3)

    def test_status_update_form_invalid_data(self):
        """ 
        Test form is valid with correct data 
        """

        form = StatusUpdateForm({
            'status': 'Resolved'
        })

        self.assertTrue(form.is_valid())

    def test_status_update_form_invalid_data(self):
        """ 
        Test form is valid with missing data 
        Test correct number of errors for required fields
        """

        form = StatusUpdateForm({})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)

    def test_maintenance_quote_form_invalid_data(self):
        """ 
        Test form is valid with missing data 
        Test correct number of errors for required fields
        """

        form = MaintenanceQuoteForm({
            'cost': 100,
            'invoice_pdf': 'testpdf.pdf',
            'paid_by': 'Tenant'
        })

        self.assertTrue(form.is_valid())

    def test_maintenance_quote_form_invalid_data(self):
        """ 
        Test form is valid with missing data 
        Test correct number of errors for required fields
        """

        form = StatusUpdateForm({})

        self.assertFalse(form.is_valid())
        self.assertEqual(len(form.errors),1)

