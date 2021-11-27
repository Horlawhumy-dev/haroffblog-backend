from django.db import models
from datetime import datetime

class SubscribedMail(models.Model):
    email = models.EmailField(null=True, blank=True)
    date_subscribed = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.email
