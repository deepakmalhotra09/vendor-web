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
    name = models.CharField(max_length=100)
    project_id = models.CharField(max_length=200, default=None)
    client_id = models.CharField(max_length=10)
    link = models.CharField(max_length=150)
    target = models.CharField(max_length=20)
    cost = models.CharField(max_length=15)
    start_date = models.DateField()
    end_date = models.DateField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class ProjectVendorAssign(models.Model):
    id = models.AutoField(primary_key=True)
    project_id = models.CharField(max_length=200, default=None)
    client_project_id = models.CharField(max_length=200)
    vendor_id = models.CharField(max_length=200)
    cost = models.CharField(max_length=15)
    links = models.TextField()
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.client_project_id

    class Meta:
        db_table = "app_project_vendor_assign"


class ProjectVendorUserAssign(models.Model):
    FORM_FILL_STATUS = (
        ('none', 'None'),
        ('completed', 'Completed'),
        ('terminated', 'Terminated'),
        ('quota_full', 'Quota Full')
    )
    id = models.AutoField(primary_key=True)
    vendor_id = models.CharField(max_length=200)
    project_id = models.CharField(max_length=200)
    client_project_id = models.CharField(max_length=200)
    user_id = models.CharField(max_length=200)
    status = models.CharField(max_length=255, choices=FORM_FILL_STATUS, default=FORM_FILL_STATUS[0][0])
    ip_address = models.CharField(max_length=255)
    create_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.id

    class Meta:
        db_table = "app_project_vendor_user_assign"
        unique_together = ('vendor_id', 'project_id', 'ip_address',)
