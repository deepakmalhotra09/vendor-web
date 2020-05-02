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
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    mobile_no = models.CharField(max_length=12)
    email = models.EmailField()
    property = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Client(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    mobile_no = models.CharField(max_length=12)
    email = models.EmailField()
    property = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    client_id = models.CharField(max_length=10)
    link = models.CharField(max_length=150)
    target = models.CharField(max_length=20)
    cost = models.CharField(max_length=15)
    start_date = models.DateField()
    end_date = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
