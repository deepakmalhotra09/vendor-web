from django.db import models
from django.utils import timezone


class Admin(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    create_time = models.DateTimeField(auto_now_add=True)

    def publish(self):
        self.create_time = timezone.now()
        self.save()


class Vendor(models.Model):
    name = models.CharField(max_length=100)
    mobile_no = models.CharField(max_length=12)
    email = models.EmailField()
    property = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
