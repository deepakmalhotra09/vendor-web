
from django.db import models
from django.utils import timezone


class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.create_time = timezone.now()
        self.save()