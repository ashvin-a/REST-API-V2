from django.db import models

# Create your models here.
class Product(models.Model):
    title = models.CharField(max_length=120)
    content = models.TextField(blank=True,null=True)
    price = models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
    
    @property
    def sale_price(self):
        return "%0.2f" %(float(self.price)*0.8)