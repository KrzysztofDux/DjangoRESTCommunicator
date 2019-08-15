from django.test import TestCase
from dispatch.models import Client
# Create your tests here.


class ClientTestCase(TestCase):

    def test_if_identity_is_set_to_correct_length(self):
        client = Client()
        self.assertEqual(len(client.identity), Client.IDENTITY_LENGTH)

