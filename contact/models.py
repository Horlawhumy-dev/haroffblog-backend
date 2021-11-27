from django.db import models
from datetime import datetime


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=250)
    email = models.EmailField()
    message = models.TextField()
    sent_date = models.DateTimeField(default=datetime.now())

    def __str__(self):
        return self.name