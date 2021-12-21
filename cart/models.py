from django.db import models
from accounts.models import NewUser
from products.models import ProductTable


# Create your models here.

class Cart(models.Model):
    user = models.ForeignKey(NewUser,default=None,on_delete=models.CASCADE,related_name='user')
    product = models.ForeignKey(ProductTable,default=None,on_delete=models.CASCADE,related_name='product')
    count = models.IntegerField(default=1)
    size = models.IntegerField(default=32)
    class Meta:
        unique_together = [("user", "product","size")]
    def __str__(self):
        return str(self.product)+", User : "+str(self.user)