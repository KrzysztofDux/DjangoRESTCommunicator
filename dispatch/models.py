from django.db import models
import random
import string


# Create your models here.
class Client(models.Model):
    IDENTITY_LENGTH = 8

    identity = models.CharField(default=''.join(random.choice(string.digits) for _ in range(IDENTITY_LENGTH)),
                                max_length=IDENTITY_LENGTH, editable=False)


class Message(models.Model):
    author = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages_authored')
    addressee = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='messages_received')
    content = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)

    @staticmethod
    def get_all_for_client(addressee):
        if isinstance(addressee, Client):
            msgs = Message.objects.filter(addressee=addressee).order_by('created')
        else:
            msgs = Message.objects.filter(addressee=Client.objects.filter(identity=addressee)).order_by('created')
        for msg in msgs:
            msg.delete()
        return msgs
