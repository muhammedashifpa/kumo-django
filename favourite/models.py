from django.db import models
from accounts.models import NewUser
from products.models import ProductTable


# Create your models here.

class Favourite(models.Model):
    user = models.ForeignKey(NewUser,default=None,on_delete=models.CASCADE)
    product = models.ForeignKey(ProductTable,default=None,on_delete=models.CASCADE)
    class Meta:
        unique_together = [("user", "product")]
    def __str__(self):
        return str(self.product)+", User : "+str(self.user)