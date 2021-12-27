from django.db import models


class Product(models.Model):
    image = models.ImageField(upload_to="product/")
    product_name=models.CharField(max_length=255)
    product_price=models.IntegerField(null=True,blank=True)
    
    def __str__(self):
        return self.product_name



