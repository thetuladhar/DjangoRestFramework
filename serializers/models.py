from django.db import models

class Address(models.Model):
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)

class Person(models.Model):
    name = models.CharField(max_length=255)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    address = models.OneToOneField(Address, on_delete=models.CASCADE, null=True, blank=True)



 