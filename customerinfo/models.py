from django.db import models

# Create your models here.
class Identity(models.Model):
    identity_name = models.CharField(max_length=100)
    identity_docs = models.TextField()

    def __str__(self):
        return self.identity_name

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    identity = models.ForeignKey(Identity, on_delete=models.CASCADE)

    def __str__(self):
        return self.name