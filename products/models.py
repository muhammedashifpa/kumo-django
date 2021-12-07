from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.db.models.fields.related import ForeignKey
from accounts.models import NewUser


class Brand(models.Model):
    brand=models.CharField(max_length=50, unique=True)
    def __str__(self):
        return self.brand


class SizeType(models.Model):
    size_types = models.CharField(max_length=200,null=False,unique=True)
    def __str__(self):
        return self.size_types

class Size(models.Model):
    size_name =  models.ForeignKey(SizeType,to_field='size_types',on_delete=models.CASCADE)
    size = models.CharField(max_length=200, unique=True)
    def __str__(self):
        return self.size
    
class ProductTable(models.Model):
    GENDER_CHOICES=(
        ('MEN','MEN'),
        ('WOMEN','WOMEN'),
        ('KIDS','KIDS'),
        ('UNISEX','UNISEX'),
    )
    CATEGORY_CHOICES=(
        ('Shirt', 'Shirt'),
        ('T Shirt', 'T Shirt'),
        ('Sport Wear', 'Sport Wear'),
        ('Out Wear', 'Out Wear'),
        ('Jackets', 'Jackets'),
        ('Trousers and shorts', 'Trousers and shorts'),
        ('Jeans', 'Jeans'),
        ('Jumpsuit', 'Jumpsuit'),
        ('Sweatshirt', 'Sweatshirt'),
        ('Jeans', 'Jeans'),
    )
    product_name = models.CharField(max_length=50,default="")
    category = models.CharField(max_length=20,choices=CATEGORY_CHOICES)  
    gender = models.CharField(max_length=20,choices=GENDER_CHOICES)  
    brand = models.ForeignKey(Brand,to_field='brand',on_delete=models.CASCADE)
    price=models.IntegerField()
    offer_price=models.FloatField(null=True)
    offer_percentage=models.FloatField(null=True)
    stock = models.IntegerField()
    description=models.TextField(max_length=500,default="")
    size_type = models.ForeignKey(SizeType,to_field='size_types',on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)
    def __str__(self):
        return str(self.product_name)

class Images(models.Model):
    product = models.ForeignKey(ProductTable, default=None, related_name='images',on_delete=models.CASCADE)
    image = models.ImageField(upload_to='prd_img', null=True, blank=True)
    def __str__(self):
        return str(self.product)
