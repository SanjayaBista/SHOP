from xml.etree.ElementInclude import default_loader
from django.db import models

# Create your models here.
class ServiceCharge(models.Model):
    SERVICE_TYPE = (
        ('PER','Percentage'),
        ('MON','Money'),
    )
    service_name = models.CharField(max_length=100)
    service_type = models.CharField(max_length=50, choices=SERVICE_TYPE, default='Money')
    rate = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.service_name

class Categories(models.Model):
    category_name = models.CharField(max_length=100)
    icon = models.ImageField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.category_name

class Brands(models.Model):
    brand_name = models.CharField(max_length=100)
    icon = models.ImageField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.brand_name

class Attributes(models.Model):
    attribute_name = models.CharField(max_length=100)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.attribute_name

class SubAttributes(models.Model):
    subattribute_name = models.ManyToManyField(Attributes)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.subattribute_name

class Colours(models.Model):
    colour_name = models.CharField(max_length=50)
    colour_code  = models.CharField(max_length=50)
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.colour_name

class Gallery(models.Model):
    image = models.ImageField(upload_to='gallery')

class Products(models.Model):
    category_name = models.ForeignKey(Categories,on_delete=models.CASCADE)
    brand_name = models.ForeignKey(Brands, on_delete=models.CASCADE)
    attribute_name = models.ForeignKey(Attributes, on_delete=models.CASCADE)
    colour_name  = models.ForeignKey(Colours, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=200)
    quantity = models.IntegerField()
    barcode = models.CharField(max_length=100)
    thumbnail = models.ImageField()
    description = models.TextField()

    def __str__(self):
        return self.product_name

