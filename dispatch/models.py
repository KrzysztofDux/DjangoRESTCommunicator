from django.db import models
import random
import string

DEFAULT_LENGTH = 8


def get_random_identity():
    return ''.join(random.choices(string.digits, k=DEFAULT_LENGTH))


# Create your models here.
class Client(models.Model):
    IDENTITY_LENGTH = DEFAULT_LENGTH

    identity = models.CharField(default=get_random_identity, max_length=IDENTITY_LENGTH, editable=False,
                                primary_key=True, unique=True)


class Message(models.Model):
    MAX_CONTENT_LENGTH = 250
    author = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages_authored')
    addressee = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages_received')
    content = models.CharField(max_length=MAX_CONTENT_LENGTH)
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_all_for_client(addressee):
        if isinstance(addressee, Client):
            msgs = Message.objects.filter(addressee=addressee).order_by('created')
        else:
            msgs = Message.objects.filter(addressee=Client.objects.get(identity=addressee)).order_by('created')
        for msg in msgs:
            msg.delete()
        return msgs