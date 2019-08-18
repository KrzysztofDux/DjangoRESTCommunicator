from django.test import TestCase
from .models import Client, Message


# Create your tests here.


class ClientTestCase(TestCase):

    def test_if_identity_is_set_to_correct_length(self):
        client = Client()
        self.assertEqual(len(client.identity), Client.IDENTITY_LENGTH)


class MessageTestCase(TestCase):

    def test_get_all_for_client_returns_all_messages(self):
        addressee = Client()
        addressee.save()

        orig_msgs = MessageTestCase.create_messages_to(addressee)

        ret_msgs = Message.get_all_for_client(addressee)

        self.assertEqual(4, ret_msgs.count())

        for ret, orig in zip(ret_msgs, orig_msgs):
            self.assertEqual(ret.content, orig.content)
            self.assertEqual(ret.author, orig.author)
            self.assertEqual(ret.addressee, orig.addressee)

    def test_get_all_for_client_deletes_messages(self):
        addressee = Client()
        addressee.save()

        MessageTestCase.create_messages_to(addressee)

        first_call_results = Message.get_all_for_client(addressee)

        second_call_results = Message.get_all_for_client(addressee)

        self.assertEqual(0, second_call_results.count())

    def test_get_all_for_client_returns_messages_for_addressee_only(self):
        addressee = Client()
        addressee.save()
        other_addressee = Client()
        other_addressee.save()

        orig_msgs = MessageTestCase.create_messages_to(addressee)
        other_msgs = MessageTestCase.create_messages_to(other_addressee)

        ret_msgs = Message.get_all_for_client(addressee)

        self.assertEqual(4, ret_msgs.count())

        for ret, orig in zip(ret_msgs, orig_msgs):
            self.assertEqual(ret.addressee, orig.addressee)

    @staticmethod
    def create_messages_to(addressee):
        author_one = Client()
        author_one.save()
        author_two = Client()
        author_two.save()

        msgs = [Message(author=author_one, addressee=addressee, content="abc"),
                Message(author=author_one, addressee=addressee, content="abcd"),
                Message(author=author_two, addressee=addressee, content="abcde"),
                Message(author=author_two, addressee=addressee, content="abcdef")]
        for msg in msgs:
            msg.save()
        return msgs


    class MessageSerializerCase(TestCase):
        