from django.db import models
from django.db.models.fields.related import RelatedField
from accounts.models import NewUser
from products.models import ProductTable

# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(NewUser,default=None,on_delete=models.CASCADE)
    order_amount = models.CharField(max_length=25)
    order_payment_id = models.CharField(max_length=100)
    isPaid = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.order_payment_id

class OrderItem(models.Model):
    order = models.ForeignKey(Order,on_delete=models.CASCADE,related_name='order_items')
    product = models.ForeignKey(ProductTable,default=None,on_delete=models.CASCADE)
    count = models.IntegerField(default=1)
    size = models.IntegerField(default=32)
    def __str__(self):
        return str(self.product)

