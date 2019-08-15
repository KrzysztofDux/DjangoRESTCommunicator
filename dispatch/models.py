from django.db import models
import random
import string


# Create your models here.
class Client(models.Model):
    IDENTITY_LENGTH = 8

    identity = models.CharField(default=''.join(random.choice(string.digits) for _ in range(IDENTITY_LENGTH)),
                                max_length=IDENTITY_LENGTH, editable=False)

