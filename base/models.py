from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Contact(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, blank=True)
    firstname = models.CharField(max_length=100, null=True)
    lastname = models.CharField(max_length=100, null=True)
    mobile_number = models.CharField(max_length=10, null=True, blank=True)
    work_number = models.CharField(max_length=10, null=True, blank=True)
    home_number = models.CharField(max_length=10, null=True, blank=True)
    email = models.EmailField(max_length = 254)
    address = models.CharField(max_length=400)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.firstname + ' ' + self.lastname

    # class Meta:
    #     ordering = ['complete']