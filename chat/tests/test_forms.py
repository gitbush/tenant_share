from django.test import TestCase
from chat.forms import MessageForm


class testForms(TestCase):
    
    def test_message_form_valid_data(self):
        """ Test form is valid with correct data """

        form = MessageForm({
                'message': 'A test message', 
        })

        self.assertTrue(form.is_valid())

    def test_message_form_invalid_with_no_data(self):
        """ Test form is invalid with missing data
            Test form displays correct error message
        """

        form = MessageForm({
                'message': '', 
        })

        self.assertFalse(form.is_valid())
        self.assertEqual(form.errors['message'], ['This field is required.'])

    