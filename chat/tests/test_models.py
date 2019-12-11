from django.test import TestCase, client
from django.urls import reverse
from chat.models import ChatMessage
from maintenance.models import MaintRequest, Rental

class TestModels(TestCase):

    def setUp(self):
        """ Create necessary instances before tests """

        self.rental = Rental(address='11 Test Street')
        self.maint_request = MaintRequest(property_ref=self.rental)
        self.chat_message = ChatMessage(maint_request=self.maint_request, message='A test message')

    def test_chat_message_is_created(self):
        """ Test a chat message instance is created """
        
        self.assertEquals(self.chat_message.maint_request.id, self.maint_request.id)
        self.assertEquals(self.chat_message.message, 'A test message')

    def test_str_is_equal_to_message(self):
        """ Test a chat message string rep is message """

        self.assertEqual(str(self.chat_message), self.chat_message.message)